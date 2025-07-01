from telebot import TeleBot
from config import API_token

bot = TeleBot(API_token)


@bot.message_handler(commands=["start"])
def welcome(message):
    # bot.send_message(message.chat.id, "welcome to microlearn bot.")
    bot.reply_to(message, "This is a reply.")


bot.polling()
