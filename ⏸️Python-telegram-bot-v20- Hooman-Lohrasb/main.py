from decouple import config

TK = config("Token")
print(TK)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello",
        reply_to_message_id=update.effective_message.id,
    )


if __name__ == "__main__":
    app = ApplicationBuilder().token(TK).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()
