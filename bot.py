from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8649850692:AAFQriunJBJucTREv-mjESa3stXVfUb0wnw"
WEB_APP_URL = "https://t.me/dogemining_app_bot/dogemine_pro"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = InlineKeyboardButton("🚀 Open App", web_app=WebAppInfo(url=WEB_APP_URL))
    await update.message.reply_text(
        "Welcome to DogeMine Pro!\nClick below to open the app:",
        reply_markup=InlineKeyboardMarkup([[button]])
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
