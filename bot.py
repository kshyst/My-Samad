import json
from typing import Final

from telegram import (
    Update,
    InlineQueryResultPhoto,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    ConversationHandler,
    filters,
    MessageHandler,
    InlineQueryHandler,
)
from decouple import config


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="به ربات سماد من خوش آمدید!",
        reply_to_message_id=update.effective_message.id,
    )


if __name__ == "__main__":
    app = ApplicationBuilder().token(config("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start_command_handler))



    app.run_polling()