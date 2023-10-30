from Participant_Class import Participant
from UTILITIES.Riot_APIS import RiotApi


class Get_Match_Data:
    def is_match_valid(self, match_data):
        game_duration = match_data['info']['gameDuration'] / 60
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
    
