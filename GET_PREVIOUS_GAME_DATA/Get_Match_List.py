from GET_PREVIOUS_GAME_DATA.Get_Match_Data import Get_Match_Data
from UTILITIES.Riot_APIS import RiotApi


class Get_Matches_List:
    def get_match_list(self, summoner_name):
        get_match_data = Get_Match_Data()
        api_client = RiotApi()
        puuid = get_match_data.get_puuid(summoner_name)
        valid_matches  = []
        match_ids = api_client.get_match_ids(puuid)
        for id in match_ids:
            match_data = get_match_data.get_match_data(id) 
            if get_match_data.is_match_valid(match_data):
                match_info = {
                    "match_id": id,
                    "match_data": match_data
                }
                valid_matches.append(match_info)
        return valid_matches