import logging
import ephem
import settings
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(stream=open(r'D:\Coding\LearnPython\lesson1\Telegram bot\bot.log', 'w', encoding='utf-8'), level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def planet_info(update, context):
    print('Вызван /planet')
    text = update.message.text
    planet = text.split()[1]
    today = date.today()
    conv_today = today.strftime("%Y/%m/%d")

    print(f'Актуальная дата {today}')

    if planet == 'Mercury':
        obj = ephem.Mercury(conv_today)
        info = ephem.constellation(obj)
        update.message.reply_text(f'Планета {planet} сейчас находится в созвездии {info}')

    elif planet == 'Venus':
        obj = ephem.Venus(conv_today)
        info = ephem.constellation(obj)
        update.message.reply_text(f'Планета {planet} сейчас находится в созвездии {info}')

    elif planet == 'Earth':
        update.message.reply_text('Соберись, мы определяем положенеи планет по отношению к Земле.')

    elif planet == 'Mars':
        obj = ephem.Mars(conv_today)
        info = ephem.constellation(obj)
        update.message.reply_text(f'Планета {planet} сейчас находится в созвездии {info}')

    elif planet == 'Jupiter':
        obj = ephem.Jupiter(conv_today)
        info = ephem.constellation(obj)
        update.message.reply_text(f'Планета {planet} сейчас находится в созвездии {info}')

    elif planet == 'Saturn':
        obj = ephem.Saturn(conv_today)
        info = ephem.constellation(obj)
        update.message.reply_text(f'Планета {planet} сейчас находится в созвездии {info}')

    elif planet == 'Uranus':
        obj = ephem.Uranus(conv_today)
        info = ephem.constellation(obj)
        update.message.reply_text(f'Планета {planet} сейчас находится в созвездии {info}')

    elif planet == 'Neptune':
        obj = ephem.Neptune(conv_today)
        info = ephem.constellation(obj)
        update.message.reply_text(f'Планета {planet} сейчас находится в созвездии {info}')
        
    else:
        update.message.reply_text('Ты уверен, что эта планета в солнечной системе?')
    
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