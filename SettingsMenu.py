import ReplyKeyboards
from telegram import (
    Update,
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
)

import CallBackQueries
import Selfs
import dicts


async def settings_command_handler_enter_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="به تنظیمات خوش آمدید!",
        reply_markup=InlineKeyboardMarkup.from_column(ReplyKeyboards.user_settings_inline_buttons)
    )


async def settings_command_handler_choose_self(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #create a self list user data in context if it does not exist #TODO databasing this
    if context.user_data.get("selfs_list") is None:
        selfs_list = Selfs.get_self_list(context.user_data["token"])
        context.user_data["selfs_list"] = selfs_list

    #create a inline button for self list
    if context.user_data["selfs_list"] is not None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="لطفا سلف مورد نظر خود را انتخاب کنید.",
            reply_markup=InlineKeyboardMarkup.from_column(
                [InlineKeyboardButton(text=str(self), callback_data=str(self)) for self in
                 context.user_data["selfs_list"]]
            )
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="خطا در دریافت لیست سلف ها!",
            reply_markup=InlineKeyboardMarkup.from_column(ReplyKeyboards.user_settings_inline_buttons)
        )


async def settings_command_handler_logout(update, context):
    pass


async def settings_command_handler_exit(update, context):
    print(context.user_data["self_ids"])
    pass
