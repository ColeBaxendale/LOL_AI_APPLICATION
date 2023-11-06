class Get_Team_Obj_Data:
    def get_team_objectives(self,match_data, team_id):
        team_id_num = 0
        if team_id == 'red':
            team_id_num = 200
        else:
            team_id_num = 100

        for team in match_data['info']['teams']:
            if team['teamId'] == team_id_num:
                objectives = team['objectives']
                return {
                    'win': team['win'],
                    'baron': objectives['baron']['kills'],
                    'dragon': objectives['dragon']['kills'],
                    'riftHerald': objectives['riftHerald']['kills'],
                    'inhibitor': objectives['inhibitor']['kills'],
                    'tower': objectives['tower']['kills']
                }

        return f"No data found for team ID {team_id}."