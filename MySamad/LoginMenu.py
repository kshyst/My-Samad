from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

import Database
import ReplyKeyboards
import Token
from dicts import USERNAME, PASSWORD, CHECK_CREDENTIALS


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
    context.user_data["password"] = password

    if Token.getTokenResponse(username, password) is not None:

        #save user credentials in database
        await Database.save_user_in_database(update, context)

        context.user_data["token"] = Token.getAccessToken(username, password)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="ورود موفقیت آمیز بود.",
            reply_to_message_id=update.effective_message.id,
            reply_markup=ReplyKeyboardMarkup(ReplyKeyboards.reply_keyboard_logged_in, one_time_keyboard=True),
        )
        return ConversationHandler.END
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="ورود ناموفق بود. لطفا دوباره تلاش کنید.",
            reply_to_message_id=update.effective_message.id,
        )
        return USERNAME
