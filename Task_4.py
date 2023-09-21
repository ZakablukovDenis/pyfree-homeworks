import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def echo(message):
    response = "Ба! Знакомые все лица!"
    bot.send_message(message.chat.id, response)


bot.polling(none_stop=True)
