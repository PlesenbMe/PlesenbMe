import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# --- Замени YOUR_TELEGRAM_BOT_TOKEN на свой токен! ---
TELEGRAM_BOT_TOKEN = "8094937290:AAEvTupF59jOnn-W7_Vv3AyDLquZlRUkWIU"


# Настройка логирования для отладки
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я твой Telegram-бот.  Напиши мне что-нибудь!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = "Я простой бот. Вот что я умею:\n"
    help_text += "/start - Начать общение.\n"
    help_text += "/help - Показать эту справку.\n"
    help_text += "Просто напиши мне что-нибудь, и я отвечу.\n"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Извини, я не понимаю эту команду.")

async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Я получил твое сообщение!")


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_command)
    caps_handler = CommandHandler('caps', caps) 
    application.add_handler(help_handler)
    application.add_handler(caps_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo) 
    application.add_handler(echo_handler)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    unknown_text_handler = MessageHandler(filters.TEXT, unknown_text)
    application.add_handler(unknown_text_handler)


    application.run_polling()