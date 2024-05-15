#!/usr/bin/python

import os
from dotenv import load_dotenv
import telebot
from random import randrange
from service.DBService import DBService
from model.Prediction import Prediction
from model.TaroCard import TaroCard

dbService = DBService()

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
bot_name = os.getenv('BOT_NAME')
bot = telebot.TeleBot(bot_token)

def send_prediction(bot, message):
    prediction = Prediction(TaroCard().service.get_random_cards())
    for i in range(len(prediction.cards)):
        file = open(f'tarot_cards/{prediction.cards[i]}', 'rb')
        bot.send_sticker(message.chat.id, file, reply_to_message_id=message.message_id)

    bot.send_message(message.chat.id, str(prediction), reply_to_message_id=message.message_id)

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