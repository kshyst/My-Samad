from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    ConversationHandler,
    filters,
    MessageHandler,
    CallbackQueryHandler,
)

import App
import CallBackQueries
import ReplyKeyboards
import dicts
import Database
import ReservedListMenu
from SettingsMenu import settings_command_handler_enter_menu
from dicts import USERNAME, PASSWORD, CHECK_CREDENTIALS
from LoginMenu import login_command_handler_username, login_command_handler_password, \
    login_command_handler_check_credentials
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #TODO change reply keyboard based on if user is logged in or not

    if context.user_data.get("token") is None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="به ربات سماد من خوش آمدید!",
            reply_to_message_id=update.effective_message.id,
            reply_markup=ReplyKeyboardMarkup(ReplyKeyboards.reply_keyboard_not_logged_in, one_time_keyboard=True),
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="به ربات سماد من خوش آمدید!",
            reply_to_message_id=update.effective_message.id,
            reply_markup=ReplyKeyboardMarkup(ReplyKeyboards.reply_keyboard_logged_in, one_time_keyboard=True),
        )

if __name__ == "__main__":
    app = App.app
    app.add_handler(CommandHandler("start", start_command_handler))
    app.add_handler(MessageHandler(filters.Text(dicts.Commands.USER_SETTINGS.value), settings_command_handler_enter_menu))
    app.add_handler(MessageHandler(filters.Text(dicts.Commands.SEE_RESERVED_LIST.value), ReservedListMenu.reserved_list_enter_menu_command_handler))

    # Callback Query Handlers
    app.add_handler(CallbackQueryHandler(CallBackQueries.user_settings_callback_handler, pattern=CallBackQueries.settings_callback_regex))
    app.add_handler(CallbackQueryHandler(CallBackQueries.exit_self_menu_handler, pattern=CallBackQueries.exit_self_menu_regex))
    app.add_handler(CallbackQueryHandler(CallBackQueries.delete_self_list_handler, pattern=CallBackQueries.delete_self_list_regex))
    # Log in Conversation
    app.add_handler(
        ConversationHandler(
            entry_points=[
                MessageHandler(filters.Text(dicts.Commands.LOG_IN_TO_SAMAD.value), login_command_handler_username)
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

    app.run_polling()
