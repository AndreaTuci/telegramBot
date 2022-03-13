import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Attivo il logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Qualche comando
def start(update, context):
    update.message.reply_text('Hi! Type / to list commands')


# Fornisce l'id della chat
def chatinfo(update, context):
    update.message.reply_text(update.message.chat.id)


# Invia il logo di Telegram
def unexpected(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo='https://static.wikia.nocookie.net/montypython/images/f/ff/Spanish_Inquisition.jpg/revision/latest?cb=20180629171423')

def show(update, context):
    context.bot.sendAnimation(chat_id=update.effective_chat.id,
                           animation='https://c.tenor.com/VFFJ8Ei3C2IAAAAM/rickroll-rick.gif')


def ni(update, context):
    update.message.reply_text("it is a good shrubbery")

# Ripete quello che dici
def echo(update, context):
    update.message.reply_text(update.message.text)


# Log degli errori
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    updater = Updater("5284401191:AAFc3Qa9kGBZr8eDGRywelldERnKFMUvwkY", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("chatinfo", chatinfo))
    dp.add_handler(CommandHandler("unexpected", unexpected))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    PORT = int(os.environ.get('PORT', '8443'))
    TOKEN = os.getenv('BOTAPIKEY')
    # updater = Updater(TOKEN)
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url="https://tuci-telegram-bot.herokuapp.com/" + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()
