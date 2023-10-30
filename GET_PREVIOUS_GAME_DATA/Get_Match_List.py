from GET_PREVIOUS_GAME_DATA.Get_Matches import Get_Match_Data
from UTILITIES.Riot_APIS import RiotApi


class Get_Matches_List:
    def get_match_list(self, summoner_name):
        get_match_data = Get_Match_Data()
        api_client = RiotApi()
        puuid = get_match_data.get_puuid(summoner_name)
        valid_matches  = []
        count = 0
        match_ids = api_client.get_match_ids(puuid)
        i = 0
        n = len(match_ids) - 1
        while count < 1 and n >= 0:
            match_data = get_match_data.get_match_data(match_ids[n]) 

            if get_match_data.is_match_valid(match_data):
                match_info = {
                    "match_id": match_ids[n],
                    "match_data": match_data
                }
                valid_matches.append(match_info)
                count += 1
            n -= 1
        return valid_matches