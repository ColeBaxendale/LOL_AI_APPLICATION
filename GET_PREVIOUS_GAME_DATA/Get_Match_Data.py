from DATA_CLASSES.Participant_Class import Participant
from UTILITIES.Riot_APIS import RiotApi
from UTILITIES.Utilities import Utilities


class Get_Match_Data:
    def is_match_valid(self, match_data):
        game_duration = Utilities.convert_time_to_game_time(match_data['info']['gameDuration'])
        if match_data['info']['queueId'] in RiotApi.RANKED_QUEUE_IDS and game_duration > 15:
            return True

    def get_match_data(self, match_id):
        api_client = RiotApi()
        match_data = api_client.get_match_details(match_id)
        return match_data
    
    def get_puuid(self, summoner_name):
     api_client = RiotApi()
     return api_client.get_puuid_by_name(summoner_name)
    
    def get_summoner_participants(self, match_data, summoner_name):
        participants = []
        participants_details = match_data['info']['participants']
        for participant in participants_details:
            participants.append(Participant(participant, summoner_name))
        return participants
    
    def cs_per_min(self, match_data, participant_id):
        participant_data = None
        game_duration = Utilities.convert_time_to_game_time(match_data['info']['gameDuration'])

        for participant in match_data['info']['participants']:
            if participant['participantId'] == participant_id:
                participant_data = participant
                break
        total_cs = participant_data['totalMinionsKilled'] + participant_data.get('neutralMinionsKilled', 0)
        cs_per_minute = total_cs / game_duration
        return round(cs_per_minute, 2) 
    
    def get_gold_per_minute(self, match_data, participant_id):
        participant_data = None
        game_duration = Utilities.convert_time_to_game_time(match_data['info']['gameDuration'])
        for participant in match_data['info']['participants']:
            if participant['participantId'] == participant_id:
                participant_data = participant
                break

        total_gold = participant_data['goldEarned']
        print(total_gold)
        gold_per_minute = total_gold / game_duration if game_duration > 0 else 0
        print(game_duration)
        return round(gold_per_minute, 2)  # Rounded to two decimal places

       
        
