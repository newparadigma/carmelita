class Prediction:
    def get_prediction_text(self):
        msg =  "Вот расклад для тебя ✨\n\n"
        msg =  msg + str(order) + '. ' + card_names[card_number].capitalize() + "\n"
        msg += "\n" + "✨✨✨✨✨✨✨✨" 
        return msg