import json
from typing import Final

from telegram import (
    Update,
    InlineQueryResultPhoto, ReplyKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    ConversationHandler,
    filters,
    MessageHandler,
    InlineQueryHandler, CallbackQueryHandler,
)
from decouple import config

import CallBackQueries
import ReplyKeyboards
import Reservation
import Token
import dicts
from SettingsMenu import settings_command_handler_enter_menu, settings_command_handler_choose_self
from dicts import USERNAME, PASSWORD, CHECK_CREDENTIALS
from LoginMenu import login_command_handler_username, login_command_handler_password, \
    login_command_handler_check_credentials
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #TODO change reply keyboard based on if user is logged in or not

    if context.user_data.get("token") is None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="به ربات سماد من خوش آمدید!",
            reply_to_message_id=update.effective_message.id,
            reply_markup=ReplyKeyboardMarkup(ReplyKeyboards.reply_keyboard_not_logged_in, one_time_keyboard=True),
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="به ربات سماد من خوش آمدید!",
            reply_to_message_id=update.effective_message.id,
            reply_markup=ReplyKeyboardMarkup(ReplyKeyboards.reply_keyboard_logged_in, one_time_keyboard=True),
        )


if __name__ == "__main__":
    app = ApplicationBuilder().token(config("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start_command_handler))
    app.add_handler(
        MessageHandler(filters.Text(dicts.Commands.USER_SETTINGS.value), settings_command_handler_enter_menu))

    # Log in Conversation
    app.add_handler(
        ConversationHandler(
            entry_points=[
                MessageHandler(filters.Text(dicts.Commands.LOG_IN_TO_SAMAD.value), login_command_handler_username)
            ],
            states={
                USERNAME: [
                    MessageHandler(filters.TEXT, login_command_handler_username)
                ],
                PASSWORD: [
                    MessageHandler(filters.TEXT, login_command_handler_password)
                ],
                CHECK_CREDENTIALS: [
                    MessageHandler(filters.TEXT, login_command_handler_check_credentials)
                ]
            },
            fallbacks=[
                #TODO implement fallback functions
                MessageHandler(filters.Text("لغو"), lambda update, context: ConversationHandler.END),
                CommandHandler("cancel", lambda update, context: ConversationHandler.END),
            ],
            allow_reentry=True,
        )
    )

    app.run_polling()
