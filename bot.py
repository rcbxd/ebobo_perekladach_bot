from googletrans import Translator
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
translator = Translator()

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    chat_type = update.message.chat.type
    language_code = update.message.from_user.language_code
    if not language_code == 'ru':
        text = translator.translate(update.message.text, dest='ru')
        msg = ''
        if chat_type == 'private':
            msg = f'{first_name} {last_name} сказал: \n{text.text}'
        else:
            msg = text.text
        update.message.reply_text(msg)


def main():
    updater = Updater("1529975202:AAE6cHICSQUauN8F3pOpfYFYFN0wFLTLdHM", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()