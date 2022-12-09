import telebot
from random import randrange

bot = telebot.TeleBot("5849685292:AAEluGxkW673fmMtDgHHQs4SqIX7F9re2uQ")

@bot.message_handler(commands=['start'])
# @bot.channel_post_handler(regexp="@carmelita_bot")

def send_cards(message):

	card_numbers = []
	while(len(card_numbers) < 3):
		card_number = randrange(77)
		if card_number not in card_numbers: card_numbers.append(card_number)

	for card_number in card_numbers:
		msg = ''
		file = open(f'tarot_cards/{card_number}.webp', 'rb')
		bot.send_photo(message.chat.id, file, msg, reply_to_message_id=message.message_id)

bot.infinity_polling()