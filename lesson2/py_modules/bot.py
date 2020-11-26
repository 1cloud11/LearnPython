import logging
import ephem
import settings
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(stream=open('bot.log', 'w', encoding='utf-8'), level=logging.INFO)

def greet_user(update, context):
    logging.info('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')

def talk_to_me(update, context):
    text = update.message.text
    update.message.reply_text(text)

def planet_info(update, context):
    logging.info('Вызван /planet')
    text = update.message.text
    command, planet = text.split()
    today = date.today()
    conv_today = today.strftime("%Y/%m/%d")

    logging.info(f'Актуальная дата {conv_today}')

    planets = {
        'Mercury': ephem.Mercury(conv_today),
        'Venus': ephem.Venus(conv_today),
        'Earth': ephem.Mars(conv_today),
        'Mars': ephem.Jupiter(conv_today),
        'Jupiter': ephem.Saturn(conv_today),
        'Saturn': ephem.Saturn(conv_today),
        'Uranus': ephem.Uranus(conv_today),
        'Neptune': ephem.Neptune(conv_today),
    }

    obj_info = planets.get(planet)
    obj_situated = ephem.constellation(obj_info)
    update.message.reply_text(f'Планета {planet} сейчас находится в созвездии {obj_situated}')
def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_info))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    
    logging.info("Бот Стартовал!")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()