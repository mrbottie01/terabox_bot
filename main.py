
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Terabox Bot! Send /link to get started.")

# /link command handler (placeholder for Terabox logic)
async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me your Terabox link...")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is not set in the environment")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("link", link))

    logger.info("Bot started.")
    app.run_polling()

if __name__ == "__main__":
    main()
