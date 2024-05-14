#!/usr/bin/python

import os
from dotenv import load_dotenv
import telebot
from random import randrange
from service.DBService import DBService

dbService = DBService()

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
bot_name = os.getenv('BOT_NAME')
bot = telebot.TeleBot(bot_token)

card_names = (
'шут',
'маг',
'жрица',
'императрица',
'император',
'жрец',
'влюблёные',
'колесница',
'сила',
'отшельник',
'фортуна',
'справедливость',
'повешенный',
'смерть',
'умеренность',
'дьявол',
'башня',
'звезда',
'луна',
'солнце',
'суд',
'мир',

'туз_жезлов',
'двойка_жезлов',
'тройка_жезлов',
'четверка_жезлов',
'пятерка_жезлов',
'шестерка_жезлов',
'семерка_жезлов',
'восьмерка_жезлов',
'девятка_жезлов',
'десятка_жезлов',
'паж_жезлов',
'рыцарь_жезлов',
'королева_жезлов',
'король_жезлов',

'туз_пентаклей',
'двойка_пентаклей',
'тройка_пентаклей',
'четверка_пентаклей',
'пятерка_пентаклей',
'шестерка_пентаклей',
'семерка_пентаклей',
'восьмерка_пентаклей',
'девятка_пентаклей',
'десятка_пентаклей',
'паж_пентаклей',
'рыцарь_пентаклей',
'королева_пентаклей',
'король_пентаклей',

'туз_кубков',
'двойка_кубков',
'тройка_кубков',
'четверка_кубков',
'пятерка_кубков',
'шестерка_кубков',
'семерка_кубков',
'восьмерка_кубков',
'девятка_кубков',
'десятка_кубков',
'паж_кубков',
'рыцарь_кубков',
'королева_кубков',
'король_кубков',

'туз_мечей',
'двойка_мечей',
'тройка_мечей',
'четверка_мечей',
'пятерка_мечей',
'шестерка_мечей',
'семерка_мечей',
'восьмерка_мечей',
'девятка_мечей',
'десятка_мечей',
'паж_мечей',
'рыцарь_мечей',
'королева_мечей',
'король_мечей',
)

i = 0
for card_name in card_names:
    print(f'{i}. {card_name}')
    os.rename(f'tarot_cards/{i}.webp','tarot_cards/' + card_name +'.webp')
    i += 1
exit()

def send_prediction(bot, message):
    card_numbers = []
    while (len(card_numbers) < 3):
        card_number = randrange(77)
        if card_number not in card_numbers:
            card_numbers.append(card_number)

    msg =  "Вот расклад для тебя ✨\n\n"
    order = 0
    for card_number in card_numbers:
        file = open(f'tarot_cards/{card_number}.webp', 'rb')
        bot.send_sticker(message.chat.id, file, reply_to_message_id=message.message_id)
        order += 1
        msg =  msg + str(order) + '. ' + card_names[card_number].capitalize() + "\n"
    msg += "\n" + "✨✨✨✨✨✨✨✨" 
    bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)

# def send_help(bot, message):
#     msg = 'Привет! Я бот, который делает расклад таро. Для того чтобы узнать свой расклад, напиши мне "расклад" или тегни меня в чате ' + '@' + bot_name + ' 🌟'
#     bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)

# расклад
@bot.message_handler(func=lambda message: message.text and bot_name in message.text)
@bot.message_handler(regexp='^[рР][аА][сС][кК][лЛ][аА][дД]$')
def get_prediction(message):
    user_id = message.from_user.id
    status = dbService.check_user_data(user_id)
    if status == 'user_not_found':
        send_prediction(bot, message)
        dbService.save_new_user(user_id)
    if status == 'allowed_to_predict':
        send_prediction(bot, message)
        dbService.update_user_last_prediction_at(user_id)
    
    if status == 'not_allowed_to_predict':
        msg = 'Колоде нужно отдохнуть 😌'
        bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)

bot.infinity_polling()