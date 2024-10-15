import re

import SettingsMenu
import Database

settings_callback_regex = re.compile("^(choose_self)|(logout)|(exit_user_menu)$")
exit_self_menu_regex = re.compile("^exit_self_menu$")
delete_self_list_regex = re.compile("^delete_self_list$")


async def user_settings_callback_handler(update, context):
    query = update.callback_query
    data = query.data

    if settings_callback_regex.match(data):
        if data == "choose_self":
            await SettingsMenu.settings_command_handler_choose_self(update, context)
        elif data == "logout":
            await SettingsMenu.settings_command_handler_logout(update, context)
        elif data == "exit_user_menu":
            await SettingsMenu.settings_command_handler_exit(update, context)
    else:
        await query.answer("دستور نامعتبر است.")
        return


async def selfs_callback_handler(update, context):
    query = update.callback_query
    data = query.data

    try:
        if context.user_data.get("selfs_list") is not None:
            if context.user_data.get("self_ids") is None:
                context.user_data["self_ids"] = []
            if data in context.user_data["selfs_list"]:
                context.user_data["self_ids"].append({data: context.user_data["selfs_list"][data]})
                await query.answer("سلف انتخاب شد.")
            else:
                await query.answer("سلف نامعتبر است.")
            print(context.user_data["self_ids"])
    except Exception as e:
        print(e)
        await query.answer("خطا در انتخاب سلف.")
        return


async def exit_self_menu_handler(update, context):
    query = update.callback_query
    data = query.data

    if exit_self_menu_regex.match(data):
        await query.answer("خروج از منوی سلف.")
        await query.message.delete()

        await Database.add_self_to_existing_user(update, context)
    else:
        await query.answer("دستور نامعتبر است.")
        return


async def delete_self_list_handler(update, context):
    query = update.callback_query
    data = query.data

    if delete_self_list_regex.match(data):
        await Database.delete_user_self_list(update, context)
        await query.answer("لیست سلف ها پاک شد.")
    else:
        await query.answer("دستور نامعتبر است.")
        return