import random
import time
import typing
from src.models.strike import LightningStrike
from datetime import datetime


class StrikeGenerator:
    def stream(self) -> typing.Iterator[LightningStrike]:
        while True:
            time.sleep(0.5)
            lat = random.uniform(-90,90)
            lon = random.uniform(-180,180)
            intensity = random.uniform(-50,200)
            timestamp = datetime.now()
            yield LightningStrike(lat=lat,lon=lon,intensity=intensity,timestamp=timestamp )