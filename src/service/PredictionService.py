from service.TaroCardService import TaroCardService
from model.Prediction import Prediction

class PredictionService:
    def __init__(self):
        self.taroCardService = TaroCardService()

    def makePrediction(self):
        cards = self.taroCardService.get_random_cards()
        return Prediction(cards)
