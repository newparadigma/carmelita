import os
from dotenv import load_dotenv
import telebot

load_dotenv()

class BotService:
    def __init__(self):
        self.bot_token = os.getenv('BOT_TOKEN')
        self.bot_name = os.getenv('BOT_NAME')
        self.bot = self.create_bot()

    def create_bot(self):
        return telebot.TeleBot(self.bot_token)

    def send_prediction(self, chat_id, reply_to_message_id, prediction):
        for i in range(len(prediction.cards)):
            file = open(f'tarot_cards/{prediction.cards[i]}', 'rb')
            self.send_sticker(chat_id, file, reply_to_message_id=reply_to_message_id)

        self.send_message(chat_id, str(prediction), reply_to_message_id=reply_to_message_id)

    def send_sticker(self, chat_id, file, reply_to_message_id):
        self.bot.send_sticker(chat_id, file, reply_to_message_id=reply_to_message_id)

    def send_message(self, chat_id, msg, reply_to_message_id):
        self.bot.send_message(chat_id, msg, reply_to_message_id=reply_to_message_id)