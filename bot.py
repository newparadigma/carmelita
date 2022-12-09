import os
from dotenv import load_dotenv
import telebot
from random import randrange

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['carmelita_bot'])
# @bot.channel_post_handler(regexp="@carmelita_bot")

def send_cards(message):

	card_numbers = []
	while(len(card_numbers) < 3):
		card_number = randrange(77)
		if card_number not in card_numbers: card_numbers.append(card_number)

	for card_number in card_numbers:
		file = open(f'tarot_cards/{card_number}.webp', 'rb')
		bot.send_sticker(message.chat.id, file, reply_to_message_id=message.message_id)

	msg = 'Вот расклад для тебя.'
	bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)

bot.infinity_polling()