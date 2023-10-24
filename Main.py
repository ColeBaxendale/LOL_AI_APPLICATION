import requests

from Fetch_Data_Riot_API import RiotApiClient
from Fetch_Recent_Game_Ids import Get_Recent_Game_Ids
from Fetch_Death_Data import Fetch_Death_Data

class Main:

    def __init__(self):
        # Initialize the Riot API client with your API key
        self.api_client = RiotApiClient()

        # Ranked queue IDs, these can be hardcoded or passed during instantiation
        self.ranked_queue_ids = [420, 440]  # Ranked Solo & Ranked Flex

        # Initialize GetInGameData with the API client and ranked queue IDs
        self.game_data_fetcher = Get_Recent_Game_Ids(self.api_client, self.ranked_queue_ids)

        # Initialize DeathAnalysis class
        self.death_analyzer = Fetch_Death_Data()

    def run(self, summoner_name):
        # Fetch match data for the given summoner
        match_ids_data = self.game_data_fetcher.fetch_data_for_summoner(summoner_name)

        for match in match_ids_data:
            match_id = match['match_id']
            match_data = self.api_client.get_match_details(match_id)

            # Extract death data for the match
            death_data = self.death_analyzer.extract_death_data(match_data, summoner_name)

            # Print out the match ID and death data
            print(f"Match ID: {match_id}")
            for death in death_data:
                print(death)
            print("\n")  # Separate different matches with a newline

if __name__ == "__main__":
    # Instantiate the main class and run the process for a specific summoner
    main_app = Main()
    main_app.run('BasicallyClutch')
