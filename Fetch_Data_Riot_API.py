import requests

class RiotApiClient:
    BASE_URL = 'https://na1.api.riotgames.com/lol/'
    API_KEY = 'RGAPI-e46bc52a-dd71-448c-9f91-30949158cd32' 
    RANKED_QUEUE_IDS = [420, 440] # 420: Ranked Solo     440: Ranked Flex

    '''
    This function fetches the PUUID (Permanent User ID) of a summoner by their summoner name.
    Params:
    - summoner_name: The name of the summoner.
    Returns:
    - The PUUID of the summoner.
    '''
    def get_puuid_by_name(self, summoner_name):
        url = f'{self.BASE_URL}summoner/v4/summoners/by-name/{summoner_name}'
        headers = {'X-Riot-Token': self.API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get("puuid")
    
    '''
    This function fetches match IDs for a given PUUID.
    Params:
    - puuid: The Permanent User ID of the summoner.
    - num_matches: The number of match IDs to retrieve.
    Returns:
    - A list of match IDs.
    '''
    def get_match_ids(self, puuid, num_matches=1):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={num_matches}'
        headers = {'X-Riot-Token': self.API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    '''
    This function fetches the details of a match by its match ID.
    Params:
    - match_id: The ID of the match.
    Returns:
    - A dictionary containing the details of the match.
    '''
    def get_match_details(self, match_id):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}'
        headers = {'X-Riot-Token': self.API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
