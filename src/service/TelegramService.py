import os
from dotenv import load_dotenv
import telebot

class TelegramService:
    def __init__(self):
        load_dotenv()
        self.bot_token = os.getenv('BOT_TOKEN')
        self.bot_name = os.getenv('BOT_NAME')
        self.bot = telebot.TeleBot(self.bot_token)
        # self.cards = self.get_card_from_dir()

    # def send_prediction(bot, message):
    #     card_numbers = []
    #     while (len(card_numbers) < 3):
    #         card_number = randrange(77)
    #         if card_number not in card_numbers:
    #             card_numbers.append(card_number)

    #     msg =  "Вот расклад для тебя ✨\n\n"
    #     order = 0
    #     for card_number in card_numbers:
    #         file = open(f'tarot_cards/{card_number}.webp', 'rb')
    #         bot.send_sticker(message.chat.id, file, reply_to_message_id=message.message_id)
    #         order += 1
    #         msg =  msg + str(order) + '. ' + card_names[card_number].capitalize() + "\n"
    #     msg += "\n" + "✨✨✨✨✨✨✨✨" 
    #     bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)

