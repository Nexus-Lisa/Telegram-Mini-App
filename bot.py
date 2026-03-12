from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8589702180:AAFJrdZ_98E_qA4enNgmQ58Zqfs6HqxOg7Q"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    button = KeyboardButton(
        text="Открыть Mini App",
        web_app=WebAppInfo(url="https://github.com/Nexus-Lisa/Telegram-Mini-App")
    )

    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True)

    await update.message.reply_text(
        "Откройте приложение",
        reply_markup=keyboard
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()