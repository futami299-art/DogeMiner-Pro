import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler

# Enable logging
logging.basicConfig(level=logging.INFO)

TOKEN = "8649850692:AAEWZbjNKQ71Uq79bBKah4VXmlkzQy_4tM0"
WEB_APP_URL = "https://t.me/dogemining_app_bot/dogemine_pro"

async def start(update, context):
    user = update.effective_user
    keyboard = [[InlineKeyboardButton("🚀 OPEN APP", web_app=WebAppInfo(url=WEB_APP_URL))]]
    
    await update.message.reply_text(
        f"⚡ Welcome to DogeMine Pro, {user.first_name}!\n\n"
        f"💰 Mine real Dogecoin\n"
        f"• 10 min mining sessions\n"
        f"• Watch videos for rewards\n"
        f"• Upgrade hashrate to Level 10\n"
        f"• Withdraw 200-1000 DOGE\n\n"
        f"👇 Click below to start mining:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    logging.info(f"User {user.id} sent /start")

async def help_command(update, context):
    await update.message.reply_text(
        "📖 Commands:\n"
        "/start - Open DogeMine Pro\n"
        "/help - Show this help"
    )

def main():
    print("🤖 DogeMine Pro Bot Starting...")
    print(f"Token: {TOKEN[:10]}...")
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    print("✅ Bot is ready! Waiting for messages...")
    app.run_polling()

if __name__ == "__main__":
    main()
