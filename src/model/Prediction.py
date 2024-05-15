class Prediction:
    def __init__(self, cards):
        self.cards = cards
        self.text1 = "Вот расклад для тебя ✨\n\n"
        self.text2 = "\n" + "✨✨✨✨✨✨✨✨"

    def __repr__(self): 
        text = self.text1
        for i in range(len(self.cards)):
            text += str(i + 1) + '. ' + self.cards[i].capitalize() + "\n"
        text += self.text2
        return text