from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from credentials import token 
from Newsfun import *
from memesfuns import get_memes , memes
from cryptoPrice import get_crypto_price , crypto_price
from vaccineUpdate import vaccineUpdate , vaccineUpdatedelhi
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    InlineQueryHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

#Logging for Debuging
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename='telegram.log',
                          filemode='a',
                          datefmt='%H:%M:%S',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update , context):
    """Send a message when the command /start is issued."""
    name = update.effective_user.first_name
    logger.info("User %s started the Bot.", name)
    start_message = ''' 
    Hi, {}
Welcome To All In One Bot.
Send /help to Check All supported Commands.

Thanks
Made by : Ayush    
    '''.format(name )
    update.effective_message.reply_text(start_message)

def help(update , context):
  teleID = update.effective_user.id
  name = update.effective_user.first_name
  logger.info("User %s and %s started the /Help Command.", name ,teleID)
  commandss = '''
/memes  : Get Latest Memes (updated Every 30 Min)

/crypto_price : Get Current Prices of CryptoCurrency 

/getvaccine : get Vaccine Update 18+ Varanasi

/vaccinedelhi : get Vaccine Update 18+ Delhi Central

/trend_news : Trending News

/ent_news : Entertainment News

/tech_news : Tech. News

Adding more Commands Soon...
  '''
  update.effective_message.reply_text(commandss)



def error(update, context):
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(token)  # create Credentials.py and add token
    dp = updater.dispatcher
    
    # Handler Are Defined Below
    dp.add_handler(CommandHandler('memes',memes))
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('memes',memes))
    dp.add_handler(CommandHandler('tech_news',tech_news))
    dp.add_handler(CommandHandler('ent_news',ent_news))
    dp.add_handler(CommandHandler('getvaccine',vaccineUpdate))
    dp.add_handler(CommandHandler('vaccinedelhi',vaccineUpdatedelhi))
    dp.add_handler(CommandHandler('trend_news',trend_news))
    dp.add_handler(CommandHandler('crypto_price',crypto_price))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


