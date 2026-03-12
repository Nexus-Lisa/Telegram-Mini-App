from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import json

TOKEN = "YOUR_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    button = KeyboardButton(
        text="Открыть приложение",
        web_app=WebAppInfo(url="https://github.com/Nexus-Lisa/Telegram-Mini-App")
    )

    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True)

    await update.message.reply_text(
        "Откройте мини приложение",
        reply_markup=keyboard
    )


async def webapp(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = json.loads(update.message.web_app_data.data)

    name = data["name"]
    text = data["text"]

    await update.message.reply_text(
        f"Новая заявка\n\nИмя: {name}\nСообщение: {text}"
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, webapp))

app.run_polling()