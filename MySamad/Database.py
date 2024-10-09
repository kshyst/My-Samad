import os
import django
from asgiref.sync import sync_to_async

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


async def add_self_to_existing_user(update: Update, context: ContextTypes.DEFAULT_TYPE, self_id: str):
    user = models.UserAccount.objects.get(telegramId=update.effective_user.id)
    for self in context.user_data["self_ids"]:
        self_name = next(key for key, value in context.user_data["selfs_list"].items() if value == self)
        user.self.add(models.Self(self_id=self, name=self_name))
