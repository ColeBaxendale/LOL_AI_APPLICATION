from UTILITIES.Utilities import Utilities


class Get_Per_Min_Data:
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
    
    def get_damage_per_min(self, match_data, participant_id):
        participant_data = None
        game_duration = Utilities.convert_time_to_game_time(match_data['info']['gameDuration'])
        for participant in match_data['info']['participants']:
            if participant['participantId'] == participant_id:
                participant_data = participant
                break
        damage_to_champs = participant_data['totalDamageDealtToChampions']
        damage_per_min = damage_to_champs / game_duration if game_duration > 0 else 0
        return round(damage_per_min, 2) 