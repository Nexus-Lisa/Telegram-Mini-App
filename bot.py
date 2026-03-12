from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import logging
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Проверка токена
if not TOKEN:
    logging.error("TELEGRAM_BOT_TOKEN не найден в .env файле!")
    exit(1)

logging.info(f"Токен загружен: {TOKEN[:10]}...")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"Получена команда /start от пользователя: {update.effective_user.id}")
    
    button = KeyboardButton(
        text="Открыть Mini App",
        web_app=WebAppInfo(url="https://github.com/Nexus-Lisa/Telegram-Mini-App")
    )

    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True)

    await update.message.reply_text(
        "Откройте приложение",
        reply_markup=keyboard
    )

def main():
    try:
        logging.info("Запуск бота...")
        app = ApplicationBuilder().token(TOKEN).build()
        
        app.add_handler(CommandHandler("start", start))
        
        logging.info("Бот запущен, ожидание сообщений...")
        app.run_polling()
        
    except Exception as e:
        logging.error(f"Ошибка запуска бота: {e}")

if __name__ == "__main__":
    main()