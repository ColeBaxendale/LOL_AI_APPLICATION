class Kill:
    def __init__(self, matchid, position, timestamp,):
        self.matchid = matchid
        self.position = position
        self.timestamp = timestamp
    
    def __str__(self):
        return (f"position: {self.position}, "
                f"timestamp: {self.timestamp}, ")
    

