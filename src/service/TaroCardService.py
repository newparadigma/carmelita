from os import listdir
from os.path import isfile, join
import random

class TaroCardService:
    def __init__(self):
        self.path = 'tarot_cards/'
        self.cards = self.get_card_from_dir()

    def get_card_from_dir(self):
        return [f for f in listdir(self.path) if isfile(join(self.path, f))]

    def get_random_cards(self, card_count = 3):
        return random.sample(self.cards, card_count)
