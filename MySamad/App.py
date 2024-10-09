from decouple import config
from telegram.ext import ApplicationBuilder

app = ApplicationBuilder().token(config("BOT_TOKEN")).build()
