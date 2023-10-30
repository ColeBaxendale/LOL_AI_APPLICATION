from UTILITIES.Riot_APIS import RiotApi


class Get_Match_Timeline:
    def get_match_timeline(self,match_id):
        api_client = RiotApi()
        match_timeline = api_client.get_match_timeline(match_id)
        return match_timeline
    
    def get_events(self, match_timeline):
        events = []
        for frame in match_timeline['info']['frames']:
            for event in frame['events']:
                events.append(event)
        return events
