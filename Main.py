from GET_PREVIOUS_GAME_DATA.Get_Matches import Get_Kills_Deaths_Assists, Get_Match_Data, Get_Match_Timeline, Get_Matches_List
from Riot_APIS import RiotApi
from RIOT_API_SERVER_STATUS.Server_Online import ServerStatusChecker


get_matches_instance = Get_Matches_List()
get_match_data_instance = Get_Match_Data()
get_match_timeline_instance = Get_Match_Timeline()
get_kills_deaths_assists_instance = Get_Kills_Deaths_Assists()


summoner_name = 'BasicallyClutch'
summoner = None

match_list_data = get_matches_instance.get_match_list(summoner_name)
for match in match_list_data:
    match_data = match["match_data"]
    participants = get_match_data_instance.get_summoner_participants(match_data,summoner_name)
    for parparticipant in participants:
        print(parparticipant)
        if parparticipant.isSummoner == True:
            summoner = parparticipant
    timeline = get_match_timeline_instance.get_match_timeline(match['match_id'])
    events = get_match_timeline_instance.get_events(timeline)
    
    kills = get_kills_deaths_assists_instance.get_kills(events, summoner.id)[0]
    deaths = get_kills_deaths_assists_instance.get_kills(events, summoner.id)[1]


    for kill in kills:
        victim_champion = participants[kill.victim_id].champion
        assist_champ_ids = kill.assisting_participant_ids
        assisting_champion = []
        if assist_champ_ids == 0:
            print(f"@ {kill.timestamp} {summoner_name} ({participants[kill.killer_id].champion}) killed {victim_champion} with no help! @ {kill.position}")
        else:
            for champId in assist_champ_ids:
                assisting_champion.append(participants[champId].champion)
            print(f"@ {kill.timestamp} {summoner_name} ({participants[kill.killer_id].champion}) killed {victim_champion} with the help of {assisting_champion}! @ {kill.position}")

    for death in deaths:
        killed_by_champion = participants[death.killer_id].champion
        assist_champ_ids = death.assisting_participant_ids
        assisting_champion = []
        if assist_champ_ids == 0:
            print(f"@ {death.timestamp} {summoner_name} ({participants[death.victim_id].champion}) died to {killed_by_champion} with no help! @ {death.position}")
        else:
            for champId in assist_champ_ids:
                assisting_champion.append(participants[champId].champion)
            
            print(f"@ {death.timestamp} {summoner_name} ({participants[death.victim_id].champion}) died to {killed_by_champion} with the help of {assisting_champion}! @ {death.position}")
