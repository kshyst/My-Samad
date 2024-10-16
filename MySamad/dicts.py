from enum import Enum


class Commands(Enum):
    LOG_IN_TO_SAMAD = "ورود به حساب سماد"
    USER_SETTINGS = "تنظیمات حساب کاربری"
    CHOOSE_SELF_SETTINGS = "انتخاب سلف ها"
    LOGOUT_SETTINGS = "خروج از حساب کاربری"
    CHARGE_ACCOUNT = "شارژ حساب"
    RESERVE_FOOD = "رزرو غذا"
    EXIT_SETTINGS = "خروج از تنظیمات"
    SEE_RESERVED_LIST = "مشاهده لیست غذا های رزرو شده"
    EXIT_SEE_RESERVED_MENU = "بازگشت به منو اصلی"


week_day_dict = {
    "satruday": "شنبه",
    "sunday": "یکشنبه",
    "monday": "دوشنبه",
    "tuesday": "سه شنبه",
    "wednesday": "چهارشنبه",
    "thursday": "پنجشنبه",
    "friday": "جمعه",
    "Saturday": "شنبه",
    "Sunday": "یکشنبه",
    "Monday": "دوشنبه",
    "Tuesday": "سه شنبه",
    "Wednesday": "چهارشنبه",
    "Thursday": "پنجشنبه",
    "Friday": "جمعه"
}

USERNAME, PASSWORD, CHECK_CREDENTIALS = range(3)
