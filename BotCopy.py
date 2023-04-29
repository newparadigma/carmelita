#!/usr/bin/python

import os
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
import asyncio
from random import randrange
import mysql.connector

mydb = mysql.connector.connect(
    host="mysql",
    user="homestead",
    password="homestead",
    database="homestead"
)

load_dotenv()

bot = AsyncTeleBot(os.getenv('BOT_TOKEN'))

cardsNames = (
'дурак', 
'верховная жриц',
'фоккусник',
'императрица',
'император',
'отшельник',
'любовники',
'колесница',
'сила',
'отшельник',
'10.web',
'11.web',
'12.web', 
'13.web',
'14.web',
'15.web',
'16.web',
'17.web',
'18.web',
'19.web',
'20.web',
'21.web',
'22.web',
'23.web',
'24.web', 
'25.web',
'26.web',
'27.web',
'28.web',
'29.web',
'30.web',
'31.web',
'32.web',
'33.web',
'34.web',
'35.web',
'36.web',
'37.web',
'38.web',
'39.web',
'40.web',
'41.web',
'42.web',
'43.web',
'44.web',
'45.web',
'46.web',
'47.web',
'48.web',
'50.web',
'50.web',
'51.web',
'52.web',
'53.web',
'54.web',
'55.web',
'56.web',
'57.web',
'58.web',
'59.web',
'60.web',
'61.web',
'62.web',
'63.web',
'64.web',
'65.web',
'66.web',
'67.web',
'68.web',
'69.web',
'70.web',
'71.web',
'72.web',
'73.web',
'74.web',
'75.web',
'76.web',
'77.web',
)

async def send_prediction(bot, message):
    card_numbers = []
    while (len(card_numbers) < 3):
        card_number = randrange(77)
        if card_number not in card_numbers:
            card_numbers.append(card_number)

    for card_number in card_numbers:
        file = open(f'tarot_cards/{card_number}.webp', 'rb')
        await bot.send_sticker(message.chat.id, file, reply_to_message_id=message.message_id)

    msg = 'Вот расклад для тебя ✨'
    await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)

def update_user(mydb, user_id):
    mycursor = mydb.cursor()
    query = "UPDATE users SET last_prediction_at = now() WHERE telegram_id = '%s';"
    mycursor.execute(query, (user_id, ))
    mydb.commit()

def save_user(mydb, user_id):
    mycursor = mydb.cursor()
    query = "INSERT INTO users (telegram_id, last_prediction_at) VALUES (%s, now())"
    mycursor.execute(query, (user_id, ))
    mydb.commit()

def get_diff(mydb, user_id):
    mycursor = mydb.cursor()
    query = "SELECT ((UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(users.last_prediction_at)) > 60 * 60 *24) as diff FROM users WHERE telegram_id = %s"
    mycursor.execute(query, (user_id, ))
    result = mycursor.fetchone()
    mydb.commit()
    return result


@bot.message_handler(commands=['carmelita_bot'])
@bot.message_handler(func=lambda message: message.text == 'расклад')
async def echo_message(message):
    user_id = message.from_user.id
    myresult = get_diff(mydb, user_id)

    if myresult is None:
        save_user(mydb, user_id)
        await send_prediction(bot, message)
    else:
        diff = myresult[0]
        if diff == 0:
            msg = 'Колоде нужно отдохнуть 😌'
            await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)
        else:
            update_user(mydb, user_id)
            await send_prediction(bot, message)

asyncio.run(bot.polling())