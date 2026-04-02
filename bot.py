from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler

TOKEN = "8649850692:AAEWZbjNKQ71Uq79bBKah4VXmlkzQy_4tM0"
WEB_APP_URL = "https://t.me/dogemining_app_bot/dogemine_pro"

async def start(update, context):
    keyboard = [[InlineKeyboardButton("🚀 Open App", web_app=WebAppInfo(url=WEB_APP_URL))]]
    await update.message.reply_text(
        "Welcome to DogeMine Pro!\nClick below to open the app:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running...")
    app.run_polling()
