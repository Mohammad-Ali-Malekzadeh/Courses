from telebot import TeleBot
from config import API_token

bot = TeleBot(API_token)

usernames = []


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "Welcome to microlearn bot")
    if message.chat.username not in usernames:
        usernames.append(message.chat.username)


@bot.message_handler(commands=["SUPU2024"])
def send_ids(message):
    for name in usernames:
        bot.send_message(message.chat.id, f"Hello {name}")


bot.polling()
