import os
import django
from asgiref.sync import sync_to_async

import Token

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MySamad.settings')
django.setup()
from telegram import Update
from telegram.ext import ContextTypes

from UserAccount import models


async def save_user_in_database(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = models.UserAccount(
        telegram_id=update.effective_user.id,
        username=context.user_data["username"],
        password=context.user_data["password"],
    )

    await sync_to_async(user.save)()


async def add_self_to_existing_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = await sync_to_async(models.UserAccount.objects.get)(telegram_id=update.effective_user.id)
    print(context.user_data["self_ids"])
    for self_dict in context.user_data["self_ids"]:
        for name, self_id in self_dict.items():
            self_instance = await sync_to_async(models.Self.objects.create)(self_id=self_id, name=name)
            await sync_to_async(user.self.add)(self_instance)

    await sync_to_async(user.save)()


async def get_selfs_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = models.UserAccount.objects.get(telegramId=update.effective_user.id)
    selfs_list = {}
    for self in user.self.all():
        selfs_list[self.name] = self.self_id
    return selfs_list


async def is_user_logged_in(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = await sync_to_async(models.UserAccount.objects.get)(telegram_id=update.effective_user.id)
        if user is not None:
            context.user_data["username"] = user.username
            context.user_data["password"] = user.password
            context.user_data["self_ids"] = [{self.name: self.self_id} for self in
                                             await sync_to_async(lambda: list(user.self.all()))()]
            context.user_data["token"] = Token.getAccessToken(user.username, user.password)
            return True
        else:
            return False
    except models.UserAccount.DoesNotExist:
        return False


async def get_user_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("username") is None:
        await is_user_logged_in(update, context)


async def delete_user_self_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = await sync_to_async(models.UserAccount.objects.get)(telegram_id=update.effective_user.id)
    for self in await sync_to_async(lambda: list(user.self.all()))():
        await sync_to_async(self.delete)()
    await sync_to_async(user.save)()
    context.user_data["self_ids"] = []
