# import os
# class Prediction:
#     def __init__(self, cards):
#         self.cards = cards
#         self.text1 = "Вот расклад для тебя ✨\n\n"
#         self.text2 = "\n" + "✨✨✨✨✨✨✨✨"

#     def __repr__(self):
#         text = self.text1
#         for i in range(len(self.cards)):
#             card_name = os.path.splitext(self.cards[i])[0].capitalize()
#             text += str(i + 1) + '. ' + card_name + "\n"
#         text += self.text2
#         return text