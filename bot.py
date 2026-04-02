import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler

# Token and URL
TOKEN = "8649850692:AAFQriunJBJucTREv-mjESa3stXVfUb0wnw"
WEB_APP_URL = "https://t.me/dogemining_app_bot/dogemine_pro"

# /start command handler
async def start(update, context):
    keyboard = [[InlineKeyboardButton("🚀 Open App", web_app=WebAppInfo(url=WEB_APP_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome to DogeMine Pro!\n\nClick below to open the app:",
        reply_markup=reply_markup
    )

# Main function
def main():
    # Create application
    application = Application.builder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    
    # Start bot
    print("🤖 Bot is running on Railway...")
    application.run_polling()

if __name__ == "__main__":
    main()
