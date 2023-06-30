#!/usr/bin/python

import os
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
import asyncio
from random import randrange
import mysql.connector

db = mysql.connector.connect(
    host="mysql",
    user="homestead",
    password="homestead",
    database="homestead"
)

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
bot_name = os.getenv('BOT_NAME')
bot = AsyncTeleBot(bot_token)

card_names = (
'шут', #0
'маг',#1
'жрица', #2
'императрица', #3
'император', #4
'жрец', #5
'влюблёные', #6
'колесница', #7
'сила', #8
'отшельник', #9
'фортуна', #10
'справедливость', #11
'повешенный', #12
'смерть', #13
'умеренность', #14
'дьявол', #15
'башня', #16
'звезда', #17
'луна', #18
'солнце', #19
'суд', #20
'мир', #21

'туз жезлов', #22
'двойка жезлов', #23
'тройка жезлов', #24
'четверка жезлов', #25
'пятерка жезлов', #26
'шестерка жезлов', #27
'семерка жезлов', #28
'восьмерка жезлов', #29
'девятка жезлов', #30
'десятка жезлов', #31
'паж жезлов', #32
'рыцарь жезлов', #33
'королева жезлов', #34
'король жезлов', #35

'туз пентаклей', #36
'двойка пентаклей', #37
'тройка пентаклей', #38
'четверка пентаклей', #39
'пятерка пентаклей', #40
'шестерка пентаклей', #41
'семерка пентаклей', #42
'восьмерка пентаклей', #43
'девятка пентаклей', #44
'десятка пентаклей', #45
'паж пентаклей', #46 
'рыцарь пентаклей', #47
'королева пентаклей', #48
'король пентаклей', #49

'туз кубков', #50
'двойка кубков', #51
'тройка кубков', #52
'четверка кубков', #53
'пятерка кубков', #54
'шестерка кубков', #55
'семерка кубков', #56
'восьмерка кубков', #57
'девятка кубков', #58
'десятка кубков', #59
'паж кубков', #60
'рыцарь кубков', #61
'королева кубков', #62
'король кубков', #63

'туз мечей', #64
'двойка мечей', #65
'тройка мечей', #66
'четверка мечей', #67
'пятерка мечей', #68
'шестерка мечей', #69
'семерка мечей', #70
'восьмерка мечей', #71
'девятка мечей', #72
'десятка мечей', #73
'паж мечей', #74
'рыцарь мечей', #75
'королева мечей', #76
'король мечей', #77
)

async def send_prediction(bot, message):
    card_numbers = []
    while (len(card_numbers) < 3):
        card_number = randrange(77)
        if card_number not in card_numbers:
            card_numbers.append(card_number)

    msg =  "Вот расклад для тебя ✨\n\n"
    order = 0
    for card_number in card_numbers:
        file = open(f'tarot_cards/{card_number}.webp', 'rb')
        await bot.send_sticker(message.chat.id, file)
        order += 1
        msg =  msg + str(order) + '. ' + card_names[card_number].capitalize() + "\n"
    msg += "\n" + "✨✨✨✨✨✨✨✨" 
    await bot.send_message(message.chat.id, msg)
     
# обновляет дату последнего предсказания пользователю по id пользователя
def update_user(db, user_id):
    cursor = db.cursor()
    query = "UPDATE users SET last_prediction_at = now() WHERE telegram_id = '%s';"
    cursor.execute(query, (user_id, ))
    db.commit()

# добавляет нового пользователя в бд с датой предсказания
def save_user(db, user_id):
    cursor = db.cursor()
    query = "INSERT INTO users (telegram_id, last_prediction_at) VALUES (%s, now())" 
    cursor.execute(query, (user_id, ))
    db.commit()

# отдает ответ на вопрос "прошло ли 24 часа с момента последнего предсказания для пользователя если он был"
def get_diff(db, user_id):
    cursor = db.cursor()
    query = "SELECT ((UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(users.last_prediction_at)) > 60 * 60 *24) as diff FROM users WHERE telegram_id = %s"
    cursor.execute(query, (user_id, ))
    result = cursor.fetchone()
    db.commit()
    return result

# расклад
@bot.message_handler(func=lambda message: message.text and bot_name in message.text)
@bot.message_handler(func=lambda message: message.text == 'расклад')
async def get_prediction(message):
    user_id = message.from_user.id
    result = get_diff(db, user_id)

    if result is None:
        save_user(db, user_id)
        await send_prediction(bot, message)
    else:
        diff = result[0]
        if diff == 0:
            msg = 'Колоде нужно отдохнуть 😌'
            await bot.send_message(message.chat.id, msg)
        else:
            update_user(db, user_id)
            await send_prediction(bot, message)

# запуск непосредственно бесконечного цикла который проверяет написал ли кто боту 
asyncio.run(bot.polling())