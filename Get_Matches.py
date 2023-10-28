from Riot_APIS import RiotApi

class Get_Matches_List:
    def get_match_list(self, summoner_name):
        get_match_data = Get_Match_Data()
        api_client = RiotApi()
        puuid = get_match_data.get_puuid(summoner_name)
        valid_match = []
        count = 0
        match_ids = api_client.get_match_ids(puuid)

        i = 0
        n = len(match_ids) - 1
        while count < 1:
            match_data = get_match_data.get_match_data(match_ids[n]) 
            if get_match_data.is_match_valid(match_data):
                valid_match.append(match_data)
                count += 1  

        return valid_match

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















class Participant:
    def __init__(self, participant_data,summoner_name):
        self.id = participant_data['participantId']
        self.name = participant_data['summonerName']
        self.champion = participant_data['championName']
        self.role = participant_data['teamPosition']
        self.team = participant_data['teamId']
        if self.team == 100:
            self.team = 'Blue'
        else:
            self.team = 'Red'
        self.isSummoner = False
        if self.name == summoner_name:
            self.isSummoner = True
        

    def __str__(self):
        return (f"ID: {self.id}, "
                f"Champion: {self.champion}, "
                f"Name: {self.name}, "
                f"Role: {self.role}, "
                f"Team: {self.team}, "
                f"{self.isSummoner}")
        
       


        

    