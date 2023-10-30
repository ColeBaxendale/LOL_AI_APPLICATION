from Participant_Class import Participant
from Riot_APIS import RiotApi
from UTILITIES.Utilities import Utilities

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
            participants.append(Participant(participant, summoner_name))
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

class Get_Kills_Deaths_Assists:
    def get_deaths(self, events, participant_id):
        deaths = []
        for event in events:
            if event['type'] == 'CHAMPION_KILL':
                if event['victimId'] == participant_id:
                    deaths.append("death")
        return deaths
    
    def get_kills(self, events, participant_id):
        kills_event = []
        deaths_event = []
        assist_event = []
        for event in events:
            if event['type'] == 'CHAMPION_KILL':
                if event['killerId'] == participant_id:   
                    kill = self.extract_kill_data(event,participant_id)
                    if kill is not None:
                        kills_event.append(kill) 
                elif event['victimId'] == participant_id:
                    death = self.extract_death_data(event,participant_id)
                    if death is not None:
                        deaths_event.append(death)
                elif 'assistingParticipantIds' in event and participant_id in event['assistingParticipantIds']:
                    assist = self.extract_assist_data(event, participant_id)
                    if assist is not None:
                        assist_event.append(assist)
        return kills_event, deaths_event, assist_event

    def extract_kill_data(self, event,participant_id):
        required_keys = ['position', 'timestamp', 'victimId']
        all_keys_except_assist = all(key in event for key in required_keys)
        has_assist = 'assistingParticipantIds' in event
        if all_keys_except_assist and has_assist:  # If both conditions are True
            
            kill = Kill(
                assisting_participant_ids=[aid - 1 for aid in event.get('assistingParticipantIds', [])],
                killer_id=participant_id,
                position=Utilities.format_position(event['position']),
                timestamp=Utilities.convert_timestamp_to_game_time(event['timestamp']),
                victim_id=event['victimId']
            )
            return kill
        elif not has_assist:
            kill = Kill(
                killer_id=participant_id,
                position=Utilities.format_position(event['position']),
                 timestamp=Utilities.convert_timestamp_to_game_time(event['timestamp']),
                victim_id=event['victimId']
            )
            return kill
        else:
            return None
        
    def extract_death_data(self, event,participant_id):
        required_keys = ['position', 'killerId', 'victimId']
        all_keys_except_assist = all(key in event for key in required_keys)
        has_assist = 'assistingParticipantIds' in event

        if all_keys_except_assist and has_assist:  # If both conditions are True
            
            kill = Kill(
                assisting_participant_ids=[aid - 1 for aid in event.get('assistingParticipantIds', [])],
                killer_id=event['killerId'],
                position=Utilities.format_position(event['position']),
                timestamp=Utilities.convert_timestamp_to_game_time(event['timestamp']),
                victim_id=participant_id
            )
            return kill
        elif not has_assist:
            kill = Kill(
                killer_id=event['killerId'],
                position=Utilities.format_position(event['position']),
                 timestamp=Utilities.convert_timestamp_to_game_time(event['timestamp']),
                victim_id=participant_id
            )
            return kill
        else:
            return None
            
    def extract_assist_data(self, event,participant_id):
        required_keys = ['position', 'killerId', 'victimId']
        all_keys_except_assist = all(key in event for key in required_keys)
        has_assist = 'assistingParticipantIds' in event

        if all_keys_except_assist and has_assist:  # If both conditions are True
            
            kill = Kill(
                assisting_participant_ids=[aid - 1 for aid in event.get('assistingParticipantIds', [])],
                killer_id=event['killerId'],
                position=Utilities.format_position(event['position']),
                timestamp=Utilities.convert_timestamp_to_game_time(event['timestamp']),
                victim_id=event['victimId']
            )
            return kill
        else:
            return None       
        
class Kill:
    def __init__(self, killer_id, position, timestamp, victim_id, assisting_participant_ids=0):
        self.killer_id = killer_id -1
        self.position = position
        self.timestamp = timestamp
        self.victim_id = victim_id - 1
        self.assisting_participant_ids = assisting_participant_ids
    
    def __str__(self):
        return (f"Assisting Ids: {self.assisting_participant_ids}, "
                f"killer_id: {self.killer_id}, "
                f"position: {self.position}, "
                f"timestamp: {self.timestamp}, "
                f"victim_id: {self.victim_id}")
    













        

        

    