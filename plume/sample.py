from dataclasses import dataclass

@dataclass
class Sample():
    timestamp: int
    payload: object
    
    def HasTimestamp(self):
        return self.timestamp is not None
