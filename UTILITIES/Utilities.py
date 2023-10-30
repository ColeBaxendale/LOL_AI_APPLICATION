class Utilities:
    @staticmethod
    def convert_timestamp_to_game_time(timestamp_ms):
        # Convert milliseconds to seconds
        timestamp_seconds = timestamp_ms // 1000  # Integer division to get total seconds
        
        # Calculate minutes and seconds from total seconds
        minutes = timestamp_seconds // 60  # Integer division to get minutes
        seconds = timestamp_seconds % 60  # Modulus to get remaining seconds
        
        # Format the time as "minutes:seconds"
        game_time = f"{minutes}:{seconds:02d}"  # Adding leading zero to seconds if needed
        return game_time

    @staticmethod
    def format_position(position):
        return f"{position['x']}, {position['y']}"
