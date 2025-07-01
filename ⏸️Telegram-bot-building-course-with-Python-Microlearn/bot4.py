from telebot import TeleBot
from config import API_token

bot = TeleBot(API_token)


# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=["start", "help"])
def handle_start_help(message):
    bot.send_message(message.chat.id, "This is a reply.")


# Handles all sent documents and audio files
@bot.message_handler(content_types=["photo"])
def handle_docs_audio(message):
    bot.send_message(message.chat.id, "This is a photo file.")


# Handles all text messages that match the regular expression
@bot.message_handler(regexp="2025")
def handle_message(message):
    bot.send_message(message.chat.id, "This  message has 2025.")


# Handles all messages for which the lambda returns True
@bot.message_handler(
    func=lambda message: message.document.mime_type == "text/plain",
    content_types=["document"],
)
def handle_text_doc(message):
    bot.send_message(message.chat.id, "This is a text document.")


# Which could also be defined as:
def test_message(message):
    return message.document.mime_type == "text/plain"


@bot.message_handler(func=test_message, content_types=["document"])
def handle_text_doc(message):
    pass


# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# This handler will be called if the message starts with '/hello' OR is some emoji
@bot.message_handler(commands=["hello"])
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == "❤️")
def send_something(message):
    pass


bot.polling()
