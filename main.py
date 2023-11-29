import telebot

bot = telebot.TeleBot('6650867535:AAEaex8VtQNllMlqldSSwVFwGOQxhsQet24')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здарова, чемпион!')


@bot.message_handler(commands=['inspireme'])
def main(message):
    bot.send_message(message.chat.id, 'Ты всё сможешь! \n*Я верю в тебя!*', parse_mode='Markdown')


@bot.message_handler(commands=['praiseme'])
def main(message):
    bot.send_message(message.chat.id, 'Ты молодец!')


@bot.message_handler(commands=['goodluck'])
def main(message):
    bot.send_message(message.chat.id, 'Желаю тебе удачи! У тебя всё получится!')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'Заряд [мотивации] на 10 часов(https://www.youtube.com/watch?v=8SaY1FirWLg)',
                     parse_mode='Markdown')


bot.infinity_polling()