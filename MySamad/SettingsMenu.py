import ReplyKeyboards
from telegram import (
    Update,
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
)

import Selfs
import Database


async def settings_command_handler_enter_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Database.get_user_info(update, context)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"کاربر تلگرام: {update.effective_user.id} \n"
             f"اکانت سماد: {context.user_data.get('username')} \n",
        reply_markup=InlineKeyboardMarkup.from_column(ReplyKeyboards.user_settings_inline_buttons)
    )


async def settings_command_handler_choose_self(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #create a self list user data in context if it does not exist #TODO databasing this
    if context.user_data.get("selfs_list") is None:
        selfs_list = Selfs.get_self_list(context.user_data["token"])
        context.user_data["selfs_list"] = selfs_list
        Selfs.create_selfs_callback_handler(selfs_list)

    #create a inline button for self list
    if context.user_data["selfs_list"] is not None:
        self_inlines = [InlineKeyboardButton(text=str(self), callback_data=str(self)) for self in context.user_data["selfs_list"]]
        self_inlines.append(InlineKeyboardButton(text="خروج و ذخیره", callback_data="exit_self_menu"))

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="لطفا سلف مورد نظر خود را انتخاب کنید.",
            reply_markup=InlineKeyboardMarkup.from_column(self_inlines)
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="خطا در دریافت لیست سلف ها!",
            reply_markup=InlineKeyboardMarkup.from_column(ReplyKeyboards.user_settings_inline_buttons)
        )


async def settings_command_handler_logout(update, context):
    print("logging out")
    pass


async def settings_command_handler_exit(update, context):
    print("exiting user menu")
    print(context.user_data["self_ids"])
    pass
