from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import Database


async def select_self_to_show_reserved(update, context):
    self_list = None

    self_list = await Database.get_selfs_list(update, context)

    if self_list is None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="شما هیچ سلفی ندارید. از تنظیمات کاربری سلف های خود را انتخاب کنید.",
            reply_markup=self_list,
        )

    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="لطفا سلف مورد نظر خود را انتخاب کنید.",
            reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(key, callback_data=value)] for key, value in self_list.items()]
            ),
        )