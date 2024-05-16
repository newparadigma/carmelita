#!/usr/bin/python

from service.UserService import UserService
from service.PredictionService import PredictionService
from service.BotService import BotService

userService = UserService()
predictionService = PredictionService()
botService = BotService()

bot = botService.bot
bot_name = botService.bot_name

# расклад
@bot.message_handler(func=lambda message: message.text and bot_name in message.text)
@bot.message_handler(regexp='^[рР][аА][сС][кК][лЛ][аА][дД]$')
def get_prediction(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    reply_to_message_id = message.message_id
    status = userService.check_user_data(user_id)

    if status == 'user_not_found':
        prediction = predictionService.makePrediction()
        botService.send_prediction(chat_id, reply_to_message_id, prediction)
        userService.save_new_user(user_id)

    if status == 'allowed_to_predict':
        prediction = predictionService.makePrediction()
        botService.send_prediction(chat_id, reply_to_message_id, prediction)
        userService.update_user_last_prediction_at(user_id)
    
    if status == 'not_allowed_to_predict':
        msg = 'Колоде нужно отдохнуть 😌'
        botService.send_message(chat_id, msg, reply_to_message_id)

    exit()

bot.infinity_polling()

# def send_help(bot, message):
#     msg = 'Привет! Я бот, который делает расклад таро. Для того чтобы узнать свой расклад, напиши мне "расклад" или тегни меня в чате ' + '@' + bot_name + ' 🌟'
#     bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id)
