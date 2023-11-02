class Utilities:
    @staticmethod
    def convert_timestamp_to_game_time(timestamp_ms):
        timestamp_seconds = timestamp_ms // 1000 
        minutes = timestamp_seconds // 60  
        seconds = timestamp_seconds % 60  
    
        game_time = f"{minutes}:{seconds:02d}"  
        return game_time

    @staticmethod
    def format_position(position):
        return f"{position['x']}, {position['y']}"
    
    @staticmethod
    def convert_time_to_game_time(game_duration):
        whole_minutes = int(game_duration // 60) 
        remaining_seconds = int(game_duration % 60) 
        game_duration = whole_minutes + remaining_seconds / 100.0
        return round(game_duration, 2)
