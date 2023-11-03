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
        
