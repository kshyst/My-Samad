from telegram import (
    Update,
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
)

import Selfs
import dicts


async def settings_command_handler_enter_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query is None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="به تنظیمات خوش آمدید!",
            reply_to_message_id=update.effective_message.id,
            reply_markup=InlineKeyboardMarkup.from_column([
                InlineKeyboardButton(text=str(dicts.Commands.CHOOSE_SELF_SETTINGS.value), callback_data="choose_self"),
                InlineKeyboardButton(text=str(dicts.Commands.LOGOUT_SETTINGS.value), callback_data="logout"),
                InlineKeyboardButton(text=str(dicts.Commands.EXIT_SETTINGS.value), callback_data="exit")
            ]
            )
        )
    elif update.callback_query.data == "choose_self":
        await settings_command_handler_choose_self(update, context)
    elif update.callback_query.data == "logout":
        await settings_command_handler_logout(update, context)
    elif update.callback_query.data == "exit":
        await settings_command_handler_exit(update, context)


async def settings_command_handler_choose_self(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selfs_list = Selfs.get_self_list(context.user_data["token"])

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="لطفا سلف مورد نظر خود را انتخاب کنید.",
        reply_to_message_id=update.effective_message.id,
    )


async def settings_command_handler_logout(update, context):
    pass


async def settings_command_handler_exit(update, context):
    pass
