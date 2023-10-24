class Fetch_Death_Data:
    def extract_death_data(self, match_data, summoner_name):
        death_data = []

        # Iterate through each participant in the match
        for participant in match_data['info']['participants']:
            if participant['summonerName'] == summoner_name:
                participant_id = participant['participantId']
                timeline = match_data['info']['frames']

                for frame in timeline:
                    if 'events' in frame:
                        for event in frame['events']:
                            if event['type'] == 'CHAMPION_KILL':
                                # Check if your summoner was the victim
                                if event['victimId'] == participant_id:
                                    death_info = {
                                        'timestamp': frame['timestamp'],
                                        'position': event['position'],
                                        'killer': None,
                                        'assists': [],
                                        'bounty': 0,
                                    }

                                    # Find the killer and assists
                                    for participant in match_data['info']['participants']:
                                        if participant['participantId'] == event['killerId']:
                                            death_info['killer'] = participant['summonerName']
                                        elif participant['participantId'] in event['assistingParticipantIds']:
                                            death_info['assists'].append(participant['summonerName'])

                                    # Check if the victim had a bounty
                                    death_info['bounty'] = participant['bounty']['totalGold']
                                    death_data.append(death_info)

        return death_data
