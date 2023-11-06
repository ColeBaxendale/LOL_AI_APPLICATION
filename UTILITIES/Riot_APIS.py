import requests


class RiotApi:
    BASE_URL = 'https://na1.api.riotgames.com/lol/'
    API_KEY = 'RGAPI-f36ac1fa-5d26-439c-a4a1-68c0e48fd117' # Add secrets
    RANKED_QUEUE_IDS = [420, 440]

    def get_puuid_by_name(self, summoner_name):
        url = f'{self.BASE_URL}summoner/v4/summoners/by-name/{summoner_name}'
        headers = {'X-Riot-Token': self.API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get("puuid")

    def get_match_ids(self, puuid, num_matches=5):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={num_matches}'
        headers = {'X-Riot-Token': self.API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    def get_match_details(self, match_id):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}'
        headers = {'X-Riot-Token': self.API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_match_timeline(self, match_id):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline'
        headers = {'X-Riot-Token': self.API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    
