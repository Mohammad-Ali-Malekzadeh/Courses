from telebot import TeleBot
from config import API_token

bot = TeleBot(API_token)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Please Enter Your name:")
    bot.register_next_step_handler(message, process_name)


def process_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"Hello {name}! How old are you?")
    bot.register_next_step_handler(message, process_age)


def process_age(message):
    age = message.text
    bot.send_message(message.chat.id, f"You are {age} years old.\n Thank you!")


bot.polling()
