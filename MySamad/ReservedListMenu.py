from telegram import (
    Update,
    ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

import Database
import ReplyKeyboards
import Token


async def reserved_list_enter_menu_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Database.get_user_info(update, context)

    self_inlines = [InlineKeyboardButton(text=str(self_id), callback_data=str(self_id)) for self_dict in
                    context.user_data["self_ids"] for self_id in self_dict.keys()]

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="لطفا سلف مورد نظر خود را انتخاب کنید.",
        reply_markup=InlineKeyboardMarkup.from_column(self_inlines)
    )
