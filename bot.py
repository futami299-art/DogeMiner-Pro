import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Bot Token
BOT_TOKEN = "8649850692:AAFQriunJBJucTREv-mjESa3stXVfUb0wnw"

# Web App URL (aapka Mini App)
WEB_APP_URL = "https://t.me/dogemining_app_bot/dogemine_pro"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_name = user.first_name
    
    # Web App button
    keyboard = [
        [InlineKeyboardButton("🚀 OPEN DOGEMINE PRO", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Welcome message
    welcome_text = f"""⚡ <b>Welcome to DogeMine Pro, {user_name}!</b> ⚡

💰 <b>Mine Real Dogecoin</b>
• 10 min mining sessions
• Watch video ads for rewards
• Upgrade hashrate to Level 10
• Withdraw 200-1000 DOGE

👇 <b>Click below to start mining!</b>"""

    await update.message.reply_text(
        welcome_text,
        parse_mode="HTML",
        reply_markup=reply_markup
    )

# /help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """📖 <b>DogeMine Pro - Game Rules</b>

⛏️ <b>Mining:</b>
• Each session lasts 10 minutes
• Mining rate increases with boost level

📺 <b>Watch Video:</b>
• 10 times per mining session
• 5 minute cooldown after limit reached
• Reward: +0.002 DOGE

⚡ <b>Boost Upgrade:</b>
• Max Level: 10
• Each level adds +0.05x to mining rate
• After Level 10: 10 min cooldown

🎁 <b>Daily Bonus:</b>
• Claim once every 24 hours
• Reward: +0.01 DOGE

💸 <b>Withdrawal:</b>
• Min: 200 DOGE | Max: 1000 DOGE
• Processing time: 20 minutes

🚀 <b>Click START to open the app!</b>"""
    
    await update.message.reply_text(help_text, parse_mode="HTML")

# Main function
def main():
    print("🤖 DogeMine Pro Bot Starting...")
    
    # Create application
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    # Start polling
    print("✅ Bot is running! Press Ctrl+C to stop.")
    app.run_polling(allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    main()
