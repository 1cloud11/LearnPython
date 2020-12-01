import logging
import re
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

import settings

#logging.basicConfig(filename='bot.log', level=logging.INFO)
logging.basicConfig(stream=open('bot.log', 'w', encoding='utf-8'), level=logging.INFO)

#PROXY = {'proxy_url': settings.PROXY_URL,
#       'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME , 'password': settings.PROXY_PASSWORD }}

def greet_user(update, context):
    logging.info('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')

def talk_to_me(update, context):
    text = update.message.text
    update.message.reply_text(text)

def word_counter_command(update, context):
    logging.info('Вызван /wordcount')
    update.message.reply_text('Сейчас посчитаем! Говори:')

def word_counter(update, context):
    text = update.message.text
    if text:
        text_list = text.split(' ')
        numbers = 0
        for word in text_list:
            try:
                if type(int(word))==int:
                    numbers+=1
            except ValueError:
                continue
        word_count = len(text_list) - numbers
        update.message.reply_text(f'Ты написал слов: {word_count}, чисел: {numbers}')
    else:
        update.message.reply_text('Нужно что-то написать.')           

def next_full_moon_coomand(update, context):
    logging.info('Вызван /fullmoon')
    today = date.today()
    conv_today = today.strftime("%Y/%m/%d")
    fullmoondata = ephem.next_full_moon(conv_today)
    update.message.reply_text(f'Ближайшее полнолуние будет {fullmoondata}')

def main():
    mybot = Updater(settings.API_KEY, use_context=True) #для исп прокси добавить аргумент request_kwargs = PROXY
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('wordcount', word_counter_command))
    dp.add_handler(CommandHandler('fullmoon', next_full_moon_coomand))
    dp.add_handler(MessageHandler(Filters.text, word_counter))
    
    logging.info("Бот Стартовал!")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()