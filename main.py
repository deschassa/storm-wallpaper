from src.engine.generator import StrikeGenerator
from src.models.strike import LightningStrike

if __name__ == "__main__":
    print("Le projet Storm démarre")
    system = StrikeGenerator()
    for i in system.stream():
        if i.is_valid():
            print(i)