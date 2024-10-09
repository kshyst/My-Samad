from telegram import InlineKeyboardButton

import dicts

reply_keyboard_logged_in = [
    ["مشاهده لیست غذا هفته بعد" , dicts.Commands.RESERVE_FOOD.value],
    [dicts.Commands.CHARGE_ACCOUNT.value, dicts.Commands.USER_SETTINGS.value],
]

reply_keyboard_not_logged_in = [
    [dicts.Commands.LOG_IN_TO_SAMAD.value]
]

user_settings_inline_buttons = [
                InlineKeyboardButton(text=str(dicts.Commands.CHOOSE_SELF_SETTINGS.value), callback_data="choose_self"),
                InlineKeyboardButton(text=str(dicts.Commands.LOGOUT_SETTINGS.value), callback_data="logout"),
                InlineKeyboardButton(text=str(dicts.Commands.EXIT_SETTINGS.value), callback_data="exit_user_menu")
]