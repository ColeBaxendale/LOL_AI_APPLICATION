from GET_PREVIOUS_GAME_DATA.Get_Matches import Get_Match_Data, Get_Match_Timeline, Get_Matches_List
from Riot_APIS import RiotApi
from RIOT_API_SERVER_STATUS.Server_Online import ServerStatusChecker


get_matches_instance = Get_Matches_List()
get_match_data_instance = Get_Match_Data()
get_match_timeline_instance = Get_Match_Timeline()



summoner_name = 'BasicallyClutch'
summoner = None

match_list_data = get_matches_instance.get_match_list(summoner_name)
for match in match_list_data:
    match_data = match["match_data"]
    participants = get_match_data_instance.get_summoner_participants(match_data,summoner_name)
    for parparticipant in participants:
        if parparticipant.isSummoner == True:
            summoner = parparticipant
        print(parparticipant)
    print(summoner)
    timeline = get_match_timeline_instance.get_match_timeline(match['match_id'])
    events = get_match_timeline_instance.get_events(timeline)
    deaths = get_match_timeline_instance.get_deaths(events, summoner.id)
    print(deaths)


    
    
    


        #         event_type = event["type"]
        #         participant_id_str = f'Participant: {event["participantId"]}' if "participantId" in event else ""
        #         timestamp = event["timestamp"]
        #         position_str = f'Position: {event["position"]}' if "position" in event else ""
                
        #         print(f'Event: {event_type} {participant_id_str} timestamp: {timestamp} {position_str}')
                
                # Uncomment below if you want to track kills by the participant
                # if event['type'] == 'CHAMPION_KILL':
                #     if event['killerId'] == participant_id:
                #         events.append("kill")

            


    























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

