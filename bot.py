from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler

TOKEN = "8649850692:AAEWZbjNKQ71Uq79bBKah4VXmlkzQy_4tM0"
WEB_APP_URL = "https://inquisitive-starship-137975.netlify.app/"  # ✅ SAHI URL

async def start(update, context):
    keyboard = [[InlineKeyboardButton("🚀 OPEN APP", web_app=WebAppInfo(url=WEB_APP_URL))]]
    await update.message.reply_text(
        "⚡ Welcome to DogeMine Pro!\n\nClick below to open the app:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running...")
    app.run_polling()
