import logging
from typing import Optional
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import subprocess
import shlex
import importlib
from functools import wraps

# load custom functions
import conf.authorization as conf_authorization


# Enable logging
#import settings
import conf.settings

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# bot access control wrapper code
def confirm_bot_authorize(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        chat_id = update.effective_chat.id
        if not str(chat_id) in conf.settings.ENABLES_CHAT_ROOMS:
            message = 'Oops.!\n\n Sorry, bot has been restricted on this room (%s).' % chat_id
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return
        return func(update, context, *args, **kwargs)
    return wrapped


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

    
@confirm_bot_authorize      #<--- restrict
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

    
@confirm_bot_authorize      #<--- restrict
def myid_command(update: Update, context: CallbackContext) -> None:
    content = 'Your Name: %s\nYour telegram Id: %s' % (update.effective_user.full_name, update.effective_user.id)
    update.message.reply_text(content)

    
def chatid_command(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    update.message.reply_text(f'Current chat_room: {chat_id}')


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater('$Your Bot_Token')

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("myid", myid_command))
    dispatcher.add_handler(CommandHandler("chatid", chatid_command))

    # on non command i.e message - echo the message on Telegram
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
