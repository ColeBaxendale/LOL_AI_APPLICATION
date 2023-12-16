class Get_Summoner_Dmg_Level:    
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
