import os
from GET_PREVIOUS_GAME_DATA.Get_Match_Data import Get_Match_Data
from GET_PREVIOUS_GAME_DATA.Get_Match_List import Get_Matches_List
from GET_PREVIOUS_GAME_DATA.Get_Kills_Deaths_Assists import Get_Kills_Deaths_Assists
from GET_PREVIOUS_GAME_DATA.Get_Per_Min_Data import Get_Per_Min_Data
from GET_PREVIOUS_GAME_DATA.Get_Summoner_Dmg_Level import Get_Summoner_Dmg_Level
from GET_PREVIOUS_GAME_DATA.Get_Team_Obj_Data import Get_Team_Obj_Data
from GET_PREVIOUS_GAME_DATA.Get_Timeline import Get_Match_Timeline
import pandas as pd


class Data_To_CSV:
    def convert_data_to_csv(self):
        get_match_list_instance = Get_Matches_List()
        get_match_data_instance = Get_Match_Data()
        get_match_timeline_instance = Get_Match_Timeline()
        get_kills_deaths_assists_instance = Get_Kills_Deaths_Assists()
        get_per_min_data_instance = Get_Per_Min_Data()
        get_summoner_dmg_level_instance = Get_Summoner_Dmg_Level()
        get_team_obj_data_instance = Get_Team_Obj_Data()
        summoner_name = 'BasicallyClutch'   
        summoner = None


        match_list_data = get_match_list_instance.get_match_list(summoner_name)
        all_matches_ids = []

        for match in match_list_data:
            summoner = None
            participants = get_match_data_instance.get_summoner_participants(match["match_data"],summoner_name)
            for parparticipant in participants:
                if parparticipant.isSummoner == True:
                    summoner = parparticipant

            timeline = get_match_timeline_instance.get_match_timeline(match['match_id'])
            events = get_match_timeline_instance.get_events(timeline)

            match_id = match['match_id']
            summoner_id = summoner.id
            summoner_champion = summoner.champion
            summoner_team = summoner.team
            summoner_level = get_summoner_dmg_level_instance.get_summoner_level(match["match_data"], summoner_id)
            total_building_dmg = get_summoner_dmg_level_instance.get_damage_to_buildings(match["match_data"], summoner_id)
            damage_to_champs = get_summoner_dmg_level_instance.get_damage_to_champions(match["match_data"], summoner_id)
            damage_per_min = get_per_min_data_instance.get_damage_per_min(match["match_data"], summoner_id)
            cs_per_minute = get_per_min_data_instance.cs_per_min(match["match_data"], summoner_id)
            gold_per_minute = get_per_min_data_instance.get_gold_per_minute(match["match_data"], summoner_id)
            teams = get_team_obj_data_instance.get_team_objectives(match["match_data"], summoner.team)
            kills, deaths, assists = get_kills_deaths_assists_instance.get_kills_deaths_assists(events, summoner.id)
            
            # Format kills, deaths, and assists
            kill_data = []
            for kill in kills:
                victim_champion = participants[kill.victim_id].champion
                assist_champ_ids = kill.assisting_participant_ids
                assisting_champions = [participants[aid].champion for aid in assist_champ_ids] if assist_champ_ids else []
                kill_data.append({
                    'timestamp': kill.timestamp,
                    'victim_champion': victim_champion,
                    'assisting_champions': assisting_champions,
                    'position': kill.position
                    })
                
            death_data = []
            for death in deaths:
                killed_by_champion = participants[death.killer_id].champion
                assist_champ_ids = death.assisting_participant_ids
                assisting_champions = [participants[aid].champion for aid in assist_champ_ids] if assist_champ_ids else []
                death_data.append({
                    'timestamp': death.timestamp,
                    'killed_by_champion': killed_by_champion,
                    'assisting_champions': assisting_champions,
                    'position': death.position
                    })
                
            assist_data = []
            for assist in assists:
                killed_by_champion = participants[assist.killer_id].champion
                victim_champion = participants[assist.victim_id].champion
                assist_champ_ids = assist.assisting_participant_ids
                assisting_champions = [participants[aid].champion for aid in assist_champ_ids if aid != summoner.id - 1]
                assist_data.append({
                    'timestamp': assist.timestamp,
                    'killed_by_champion': killed_by_champion,
                    'victim_champion': victim_champion,
                    'assisting_champions': assisting_champions,
                    'position': assist.position,
                })

            match_directory = f'MATCHES_CSV/MATCH_{match_id}'
            if not os.path.exists(match_directory):
                os.makedirs(match_directory)

            kills_filename = os.path.join(match_directory, f'{match_id}_kills.csv')
            deaths_filename = os.path.join(match_directory, f'{match_id}_deaths.csv')
            assists_filename = os.path.join(match_directory, f'{match_id}_assists.csv')
            pd.DataFrame(kill_data).to_csv(kills_filename, index=False)
            pd.DataFrame(death_data).to_csv(deaths_filename, index=False)
            pd.DataFrame(assist_data).to_csv(assists_filename, index=False)

            
            # Create a dictionary for each match
            match_data_dict = {
                'MatchID': match_id,

                'SummonerID': summoner_id,
                'SummonerTeam': summoner_team,
                'Champion': summoner_champion,

                'Level': summoner_level,
                'TotalBuildingDamage': total_building_dmg,
                'DamageToChampions': damage_to_champs,

                'DamagePerMinute': damage_per_min,
                'CSPerMinute': cs_per_minute,
                'GoldPerMinute': gold_per_minute,

                'KillsFilename': kills_filename,
                'DeathsFilename': deaths_filename,
                'AssistsFilename': assists_filename,


                'BaronKills': teams.get('baron', 0),
                'DragonKills': teams.get('dragon', 0),
                'RiftHeraldKills': teams.get('riftHerald', 0),
                'InhibitorKills': teams.get('inhibitor', 0),
                'TowerKills': teams.get('tower', 0),

                'Win': teams.get('win', False)
                
            }

            all_matches_ids.append(match_id)
            print(f'{match_id} appended')
            match_summary_csv_path = f'{match_directory}/{match_id}_SUMMARY.csv'
            pd.DataFrame([match_data_dict]).to_csv(match_summary_csv_path, index=False)
            print(f'Match summary CSV created for match ID {match_id} at {match_summary_csv_path}')
            
        summary_csv_path = 'MATCHES_CSV/MATCHES_IDS.csv'
        if not os.path.exists('MATCHES_CSV'):
            os.makedirs('MATCHES_CSV')
        matches_ids_df = pd.DataFrame({'MATCH_ID': all_matches_ids})
        matches_ids_df.to_csv(summary_csv_path, index=False)
        print(f'Summary CSV created at {summary_csv_path}')
        