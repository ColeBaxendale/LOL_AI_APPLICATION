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
