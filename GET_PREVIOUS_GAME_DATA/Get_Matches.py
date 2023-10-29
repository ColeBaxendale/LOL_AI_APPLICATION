from Participant_Class import Participant
from Riot_APIS import RiotApi

class Get_Matches_List:
    def get_match_list(self, summoner_name):
        get_match_data = Get_Match_Data()
        api_client = RiotApi()
        puuid = get_match_data.get_puuid(summoner_name)
        valid_matches  = []
        count = 0
        match_ids = api_client.get_match_ids(puuid)
        i = 0
        n = len(match_ids) - 1
        while count < 1 and n >= 0:
            match_data = get_match_data.get_match_data(match_ids[n]) 

            if get_match_data.is_match_valid(match_data):
                match_info = {
                    "match_id": match_ids[n],
                    "match_data": match_data
                }
                valid_matches.append(match_info)
                count += 1
            n -= 1
        return valid_matches

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
            participants .append(Participant(participant, summoner_name))
        return participants
    
class Get_Match_Timeline:
    
    def get_match_timeline(self,match_id):
        api_client = RiotApi()
        match_timeline = api_client.get_match_timeline(match_id)
        return match_timeline
    
    def get_events(self, match_timeline):
        events = []
        for frame in match_timeline['info']['frames']:
            for event in frame['events']:
                events.append(event)
        return events


    def get_deaths(self, events, participant_id):
        deaths = []
        for event in events:
            if event['type'] == 'CHAMPION_KILL':
                if event['victimId'] == participant_id:
                    deaths.append("death")
        return deaths
    
    def get_kills(self, events, participant_id):
        kills = []
        for event in events:
            if event['type'] == 'CHAMPION_KILL':
                if event['killerId'] == participant_id:
                    kills.append("kill")
        return kills
    
    def get_assists(self, events, participant_id):
        assists = []
        for event in events:
            if event['type'] == 'CHAMPION_KILL' and 'assistingParticipantIds' in event:
                if participant_id in event['assistingParticipantIds']:
                    assists.append("assist")
        return assists
    















        

        

    