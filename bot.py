import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

# Token do seu bot Telegram
TOKEN = "7502128435:AAG9Txh3ewCNg4xN5AxTvKig3bLsMqURPbU"

# Dicionário de keys válidas
VALID_KEYS = {
    "ABC123": {"used": False, "days": 3},
    "KEY456": {"used": False, "days": 5},
    "FREE789": {"used": False, "days": 7}
}

# Link do seu jogo
GAME_LINK = "https://www.mediafire.com/file/wdukeh6yzuckvw0/FFH4X_%2540LUXECHEATS.zip/file"

# Configuração de logs
logging.basicConfig(level=logging.INFO)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Olá! Use /getlink <sua_key> para acessar o jogo.")

# Comando /getlink <key>
async def getlink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("❌ Use o comando assim: /getlink SUA_KEY")
        return

    user_key = context.args[0]
    if user_key in VALID_KEYS:
        key_data = VALID_KEYS[user_key]
        if key_data["used"]:
            await update.message.reply_text("⚠️ Essa key já foi usada.")
        else:
            key_data["used"] = True
            validade = datetime.datetime.now() + datetime.timedelta(days=key_data["days"])
            await update.message.reply_text(f"✅ Key aceita! Link do jogo:
{GAME_LINK}

Validade: {validade.strftime('%d/%m/%Y')}")
    else:
        await update.message.reply_text("❌ Key inválida.")

# Inicialização do bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getlink", getlink))
    app.run_polling()

if __name__ == "__main__":
    main()
