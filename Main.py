from Riot_APIS import RiotApi
from RIOT_API_SERVER_STATUS.Server_Online import ServerStatusChecker



class MyApp:
    def __init__(self):
        self.server_checker = ServerStatusChecker()
        self.riot_api = RiotApi()

    def run(self):
        if self.server_checker.server_online():
            print('RUN PROGRAM')
        else:
            print("Sorry, a server is offline; cannot get data")

if __name__ == "__main__":
    app = MyApp()
    app.run()





# summoner_name = 'BasicallyClutch'
# api_client = RiotApi()
# puuid = api_client.get_puuid_by_name(summoner_name)
# print(f"PUUID: {puuid}")
# match_ids = api_client.get_match_ids(puuid)

# for match_id in match_ids:
#     match_data = api_client.get_match_details(match_id)

#     game_duration = match_data['info']['gameDuration'] / 60
#     if match_data['info']['queueId'] in RiotApi.RANKED_QUEUE_IDS and game_duration > 15:
#         print(f"MATCH IDS: {match_id}") # 1 match
#         participant_id = None
#         match_timeline = api_client.get_match_timeline(match_id)
#         events = []
#         for participant in match_timeline['info']['participants']:
#             if participant['puuid'] == puuid:
#                 participant_id = participant['participantId']
#         print(participant_id)
#         for frame in match_timeline['info']['frames']:
#             for event in frame['events']:
#                 if event['type'] == 'CHAMPION_KILL':
#                     if event['killerId'] == participant_id:
#                         events.append("kill")

#         print(events)
            


    























# api_client = RiotApiClient()

# # Fetch the PUUID for the summoner with the name 'BasicallyClutch'
# puuid = api_client.get_puuid_by_name('BasicallyClutch')

# # Fetch the match IDs for the retrieved PUUID
# match_ids = api_client.get_match_ids(puuid)

# # Iterate over each match ID
# for match_id in match_ids:

#     # Fetch detailed information for each match
#     match_data = api_client.get_match_details(match_id)
    
#     match_timeline = api_client.get_match_timeline(match_id)

#     # Convert the game duration from seconds to minutes
#     game_duration = match_data['info']['gameDuration'] / 60  
    
#     # Filter out non-ranked matches and matches that lasted less than 15 minutes
#     if match_data['info']['queueId'] in RiotApiClient.RANKED_QUEUE_IDS and game_duration > 15:
#         participant_id = api_client.get_most_recent_match_participant_id(summoner_name)
#         # Iterate over each participant in the match
#         for participant in match_data['info']['participants']:
#             # Check if the current participant is the summoner we are interested in
#             if participant['summonerName'] == 'BasicallyClutch':
#                 # Extract KDA, damage dealt to champions, and vision score for the summoner
#                 kda = (participant['kills'], participant['deaths'], participant['assists'])
#                 damage = participant['totalDamageDealtToChampions']
#                 vision = participant['visionScore']
                
#                 # Print the retrieved statistics for the summoner
#                 print(f"Match ID: {match_id}, KDA: {kda}, Damage: {damage}, Vision: {vision}")

