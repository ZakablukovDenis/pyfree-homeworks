import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

my_name = 'Denis'


@bot.message_handler(content_types=["text"])
def echo(message):
    if my_name in message.text:
        text = 'Ба! Знакомые все лица'
    else:
        text = message.text

    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
