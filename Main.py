from GET_PREVIOUS_GAME_DATA.Get_Match_Data import Get_Match_Data
from GET_PREVIOUS_GAME_DATA.Get_Match_List import Get_Matches_List
from GET_PREVIOUS_GAME_DATA.Get_Kills_Deaths_Assists import Get_Kills_Deaths_Assists
from GET_PREVIOUS_GAME_DATA.Get_Timeline import Get_Match_Timeline






get_match_list_instance = Get_Matches_List()
get_match_data_instance = Get_Match_Data()
get_match_timeline_instance = Get_Match_Timeline()
get_kills_deaths_assists_instance = Get_Kills_Deaths_Assists()


summoner_name = 'BasicallyClutch'
summoner = None

match_list_data = get_match_list_instance.get_match_list(summoner_name)
for match in match_list_data:
    match_data = match["match_data"]
    participants = get_match_data_instance.get_summoner_participants(match_data,summoner_name)
    for parparticipant in participants:
        print(parparticipant)
        if parparticipant.isSummoner == True:
            summoner = parparticipant
    timeline = get_match_timeline_instance.get_match_timeline(match['match_id'])
    events = get_match_timeline_instance.get_events(timeline)
    
    kills, deaths, assists = get_kills_deaths_assists_instance.get_kills_deaths_assists(events, summoner.id)


    print(f"\n\n\n")
    print("KILLS")
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
    print(f"\n\n\n")
    print("DEATHS")
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
    
    print(f"\n\n\n")
    print("ASSISTS")
    for assist in assists:
        only_assist = False
        killed_by_champion = participants[assist.killer_id ].champion
        victim_champion = participants[assist.victim_id].champion
        assist_champ_ids = assist.assisting_participant_ids
        assisting_champion = []
        if len(assist_champ_ids) == 1:
            for champId in assist_champ_ids:
                if champId is summoner.id-1:
                    only_assist = True
                else:
                    assisting_champion.append(participants[champId].champion)
        else:
            for champId in assist_champ_ids:
                if champId is not summoner.id-1:
                    assisting_champion.append(participants[champId].champion)
        if only_assist:
            print(f"@ {assist.timestamp} {summoner_name} ({participants[summoner.id-1].champion}) helped {killed_by_champion} kill {victim_champion} with no more help! @ {assist.position}")
        else:
            print(f"@ {assist.timestamp} {summoner_name} ({participants[summoner.id-1].champion}) helped {killed_by_champion} kill {victim_champion} with more help from {assisting_champion}! @ {assist.position}")

    

    cs_per_minute = get_match_data_instance.cs_per_min(match["match_data"], summoner.id)
    gold_per_minute = get_match_data_instance.get_gold_per_minute(match["match_data"], summoner.id)
    print(f"{cs_per_minute} farm per minute")
    print(f"{gold_per_minute} gold per minute")
