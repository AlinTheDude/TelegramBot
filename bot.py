import logging
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "8064799100:AAGbCZh1TZuECdXK8rg4pooBiJSRBU_dR7o"

async def start(update, context):
    await update.message.reply_text("Ciao! Sono attivo.")

async def help_command(update, context):
    await update.message.reply_text("Comandi disponibili:\n/start - Avvia\n/help - Aiuto")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
