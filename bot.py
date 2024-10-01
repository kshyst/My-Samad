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
    InlineQueryHandler,
)
from decouple import config

import ReplyKeyboards
import Token

USERNAME, PASSWORD, CHECK_CREDENTIALS = range(3)


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #TODO change reply keyboard based on if user is logged in or not

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="به ربات سماد من خوش آمدید!",
        reply_to_message_id=update.effective_message.id,
        reply_markup=ReplyKeyboardMarkup(ReplyKeyboards.reply_keyboard_not_logged_in, one_time_keyboard=True),
    )


async def login_command_handler_username(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="لطفا نام کاربری حساب سماد خود را وارد کنید.",
        reply_to_message_id=update.effective_message.id,
    )

    return PASSWORD


async def login_command_handler_password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["username"] = update.effective_message.text

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="لطفا رمز عبور حساب سماد خود را وارد کنید.",
        reply_to_message_id=update.effective_message.id,
    )

    return CHECK_CREDENTIALS


async def login_command_handler_check_credentials(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    username = context.user_data["username"]
    password = update.effective_message.text

    if Token.getTokenResponse(username, password) is not None:
        #TODO save user credentials in database

        context.user_data["token"] = Token.getAccessToken(username, password)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="ورود موفقیت آمیز بود.",
            reply_to_message_id=update.effective_message.id,
            reply_keyboard_markup=ReplyKeyboardMarkup(ReplyKeyboards.reply_keyboard_logged_in, one_time_keyboard=True),
        )
        return ConversationHandler.END
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="ورود ناموفق بود. لطفا دوباره تلاش کنید.",
            reply_to_message_id=update.effective_message.id,
        )
        return USERNAME




if __name__ == "__main__":
    app = ApplicationBuilder().token(config("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start_command_handler))

    # Log in Conversation
    app.add_handler(
        ConversationHandler(
            entry_points=[
                MessageHandler(filters.Text("ورود به حساب سماد"), login_command_handler_username)
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

    #See Reservation Options Conversation
    app.add_handler(
        ConversationHandler(
            entry_points=[

            ],
            states={

            },
            fallbacks=[

            ],
            allow_reentry=True,
        )
    )
    app.run_polling()
