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