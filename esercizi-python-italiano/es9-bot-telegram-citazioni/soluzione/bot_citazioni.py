# Bot Telegram Citazioni - SOLUZIONE
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
import random

load_dotenv()

CITAZIONI = {
    "Dante Alighieri": [
        "Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura",
        "Amor, ch'al cor gentil ratto s'apprende",
        "Lasciate ogni speranza, voi ch'entrate"
    ],
    "Alessandro Manzoni": [
        "Il buon senso c'era, ma se ne stava nascosto per paura del senso comune",
        "Ai posteri l'ardua sentenza"
    ],
    "Giacomo Leopardi": [
        "Sempre caro mi fu quest'ermo colle",
        "E il naufragar m'è dolce in questo mare"
    ],
    "Italo Calvino": [
        "Chi siamo noi, chi è ciascuno di noi se non una combinatoria di esperienze",
        "Un classico è un libro che non ha mai finito di dire quel che ha da dire"
    ],
    "Giuseppe Ungaretti": [
        "M'illumino d'immenso",
        "Si sta come d'autunno sugli alberi le foglie"
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Bot Citazioni Letterarie Italiane\n\n"
        "Comandi:\n"
        "/citazione - Citazione casuale\n"
        "/autore <nome> - Citazioni di un autore\n"
        "/help - Aiuto"
    )

async def citazione_casuale(update: Update, context: ContextTypes.DEFAULT_TYPE):
    autore = random.choice(list(CITAZIONI.keys()))
    citazione = random.choice(CITAZIONI[autore])
    await update.message.reply_text(f"💭 \"{citazione}\"\n\n— {autore}")

async def citazione_autore(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usa: /autore <nome autore>")
        return

    nome_autore = ' '.join(context.args).title()
    if nome_autore in CITAZIONI:
        citazione = random.choice(CITAZIONI[nome_autore])
        await update.message.reply_text(f"💭 \"{citazione}\"\n\n— {nome_autore}")
    else:
        await update.message.reply_text(
            f"Autore '{nome_autore}' non trovato.\n"
            f"Autori disponibili: {', '.join(CITAZIONI.keys())}"
        )

def main():
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    if not TOKEN:
        print("❌ Token non trovato! Crea file .env con TELEGRAM_BOT_TOKEN")
        return

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("citazione", citazione_casuale))
    app.add_handler(CommandHandler("random", citazione_casuale))
    app.add_handler(CommandHandler("autore", citazione_autore))

    print("🤖 Bot avviato...")
    app.run_polling()

if __name__ == "__main__":
    main()
