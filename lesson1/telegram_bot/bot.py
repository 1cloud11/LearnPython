import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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

def main():
    mybot = Updater(settings.API_KEY, use_context=True) #для исп прокси добавить аргумент request_kwargs = PROXY
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот Стартовал!")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()