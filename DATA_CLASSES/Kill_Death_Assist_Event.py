class Kill:
    def __init__(self, killer_id, position, timestamp, victim_id, assisting_participant_ids=0):
        self.killer_id = killer_id -1
        self.position = position
        self.timestamp = timestamp
        self.victim_id = victim_id - 1
        self.assisting_participant_ids = assisting_participant_ids
    
    def __str__(self):
        return (f"Assisting Ids: {self.assisting_participant_ids}, "
                f"killer_id: {self.killer_id}, "
                f"position: {self.position}, "
                f"timestamp: {self.timestamp}, "
                f"victim_id: {self.victim_id}")
    

