from UTILITIES.Utilities import Utilities


class Methods_To_Sort:
    
    def cs_per_min(self, match_data, participant_id):
        participant_data = None
        game_duration = Utilities.convert_time_to_game_time(match_data['info']['gameDuration'])

        for participant in match_data['info']['participants']:
            if participant['participantId'] == participant_id:
                participant_data = participant
                break
        total_cs = participant_data['totalMinionsKilled'] + participant_data.get('neutralMinionsKilled', 0)
        cs_per_minute = total_cs / game_duration
        return round(cs_per_minute, 2) 
    
    def get_gold_per_minute(self, match_data, participant_id):
        participant_data = None
        game_duration = Utilities.convert_time_to_game_time(match_data['info']['gameDuration'])
        for participant in match_data['info']['participants']:
            if participant['participantId'] == participant_id:
                participant_data = participant
                break
        total_gold = participant_data['goldEarned']
        gold_per_minute = total_gold / game_duration if game_duration > 0 else 0
        return round(gold_per_minute, 2) 
    
    def get_summoner_level(self, match_data, participant_id):
        participant_data = None
        for participant in match_data['info']['participants']:
            if participant['participantId'] == participant_id:
                participant_data = participant
                break
        summoner_level = participant_data['champLevel']
        return(summoner_level)
    
    def get_damage_to_buildings(self, match_data, participant_id):
        participant_data = None
        for participant in match_data['info']['participants']:
            if participant['participantId'] == participant_id:
                participant_data = participant
                break
        damage_dealt_to_buildings = participant_data['damageDealtToBuildings']
        damage_dealt_to_turrents = participant_data['damageDealtToTurrets']
        total_building_dmg = damage_dealt_to_buildings + damage_dealt_to_turrents
        return(total_building_dmg)   
        
    def get_damage_to_champions(self, match_data, participant_id):
        participant_data = None
        for participant in match_data['info']['participants']:
            if participant['participantId'] == participant_id:
                participant_data = participant
                break
        damage_to_champs = participant_data['totalDamageDealtToChampions']
        return(damage_to_champs)   
        
    def get_team_objectives(self,match_data, team_id):
        team_id_num = 0
        if team_id == 'red':
            team_id_num = 200
        else:
            team_id_num = 100


        # Check if 'info' key is present in match_data
        if 'info' not in match_data:
            return "No 'info' key found in match_data"
    
        # Check if 'teams' key is present within 'info'
        if 'teams' not in match_data['info']:
            return "No 'teams' key found in match_data['info']"
    
        # Iterate through the teams in the match_data
        for team in match_data['info']['teams']:
            if team['teamId'] == team_id_num:
                # Extract the objectives
                objectives = team['objectives']
                return {
                    'win': team['win'],
                    'baron': objectives['baron']['kills'],
                    'dragon': objectives['dragon']['kills'],
                    'riftHerald': objectives['riftHerald']['kills'],
                    'inhibitor': objectives['inhibitor']['kills'],
                    'tower': objectives['tower']['kills']
                }
    
        # If the teamId was not found in the teams list
        return f"No data found for team ID {team_id}."

