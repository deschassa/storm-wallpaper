from dataclasses import dataclass
from datetime import datetime

@dataclass
class LightningStrike:
    lon:float
    lat:float
    intensity:float
    timestamp: datetime
    def is_valid(self):
        if self.lon<-180 or self.lon>180 or self.lat<-90 or self.lat>90:
            return False
        return True

