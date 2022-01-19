import telebot

from config import token, keys
from extensions import ExchangeException, Exchange

TOKEN = "5045280121:AAEIujhiMEfPo7JhwFiMTJoJCAnbKAMHLMY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    text = 'Доброго времени суток, с вами Банко-Бот.\n- Показать список доступных валют через команду /values \
        \n- Вывести конвертацию валюты через команду <валюта> <валюта для перевода> <количество>\n \
    - Напомнить, что я могу через команду /help'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ExchangeException('Введите команду или 3 параметра')

        quote, base, amount = values
        total_base = Exchange.get_price(quote, base, amount)
    except ExchangeException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Что-то пошло не так с {e}')
    else:
        text = f'Переводим {base} в {quote}\n{amount} у.е. = {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)