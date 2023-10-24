class Get_Recent_Game_Ids:
    def __init__(self, api_client, ranked_queue_ids):
        self.api_client = api_client
        self.ranked_queue_ids = ranked_queue_ids

    def fetch_data_for_summoner(self, summoner_name):
        puuid = self.api_client.get_puuid_by_name(summoner_name)
        match_ids = self.api_client.get_match_ids(puuid)
        
        return [data for data in (self.process_match_data(match_id) for match_id in match_ids) if data]

    def process_match_data(self, match_id):
        match_data = self.api_client.get_match_details(match_id)
        
        if self.is_valid_match(match_data):
            return self.extract_match_id(match_id)
        return None

    def is_valid_match(self, match_data):
        game_duration = match_data['info'].get('gameDuration', 0) / 60
        return match_data['info']['queueId'] in self.ranked_queue_ids and game_duration > 15

    def extract_match_id(self, match_id):
        return {
            "match_id": match_id
        }
