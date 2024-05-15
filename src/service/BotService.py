from service.TelegramService import TelegramService

class BotService:
    def __init__(self):
        self.telegram_service = TelegramService()

    def send_prediction(bot, message):
        # return self.telegram_service.send_prediction(bot, message)