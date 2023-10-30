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
    
        
