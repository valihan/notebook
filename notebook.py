#!/usr/bin/python
import telebot
import config
import constant
from db import cl_db
from class_main import cl_main

go_bot = telebot.TeleBot(config.API_TOKEN)
go_main = cl_main()


# Handle '/start'
@go_bot.message_handler(commands=['start'])
def start(message):
    print("start:", message.from_user.first_name,message.date)
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row(constant.log_day, constant.log_week, constant.log_month)
    go_bot.reply_to(message, go_main.start(message), reply_markup=keyboard) 


@go_bot.message_handler(commands=['debug1'])
def debug(message):
    go_bot.reply_to(message, go_main.switch_debug())


@go_bot.message_handler(commands=['debug9'])
def debug(message):
    go_bot.reply_to(message, go_main.switch_debug9())


@go_bot.message_handler(commands = ['history', 'h'] )
def history(message):
    print("history")
    go_bot.reply_to(message, go_main.history(message))


@go_bot.message_handler(func=lambda message: True)
def main(message):
    if message.text == '':
        return

    if message.text == constant.log_day:
        go_bot.reply_to(message, go_main.log_day(message))
        return
    elif message.text == constant.log_week:
        go_bot.reply_to(message, go_main.log_week(message))
        return
    elif message.text == constant.log_month:
        go_bot.reply_to(message, go_main.log_month(message))
        return
    elif message.text == constant.log_year:
        go_bot.reply_to(message, go_main.log_year(message))
        return
    try:
        lv_response = go_main.main(message)
        go_bot.reply_to( message, lv_response )
    except:
        go_bot.reply_to( message, constant.gc_msg_error )

go_bot.infinity_polling()
