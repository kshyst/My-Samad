import dicts

reply_keyboard_logged_in = [
    ["مشاهده لیست غذا هفته بعد" , dicts.Commands.RESERVE_FOOD.value],
    [dicts.Commands.CHARGE_ACCOUNT.value, dicts.Commands.USER_SETTINGS.value],
]

reply_keyboard_not_logged_in = [
    [dicts.Commands.LOG_IN_TO_SAMAD.value]
]

