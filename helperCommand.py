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

/crypto_price : Get Current Prices of CryptoCurrency(Not Working) 

/getvaccine : get Vaccine Update 18+ Varanasi

/vaccinedelhi : get Vaccine Update 18+ Delhi Central

/trend_news : Trending News

/ent_news : Entertainment News

/tech_news : Tech. News

/udemycoupon : get links Paid Udemy courses that are FREE now

/torrent : get torrent magnet Links( /torrent SearchQuery)

/watchtowatch : get Where movie/show is available( /watchtowatch MOVIE_NAME)

Adding more Commands Soon...
  '''
  update.effective_message.reply_text(commandss)



def error(update, context):
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, context.error)



def torrentError(update, context):
  logger.info("User %s %s send wrong torrent command '%s'", update.effective_user.first_name,update.effective_user.id , update.effective_message.text)
  reply_text = """ILLEGAL INPUT.
correct Format : /torrent SearchQuery
  
eg.
/torrent Spider man
/torrent Avengers
"""
  update.message.reply_text(reply_text)

def watchError(update, context):
  logger.info("User %s %s send wrong wheretowatch command '%s'", update.effective_user.first_name,update.effective_user.id , update.effective_message.text)
  reply_text = """ILLEGAL INPUT.
correct Format : /wheretowatch MOVIE_NAME
  
eg.
/wheretowatch Spider man
/wheretowatch batman
"""
  update.message.reply_text(reply_text)
  
def wrongCommend(update, context):
  logger.info("User %s %s send wrong command '%s'", update.effective_user.first_name,update.effective_user.id,update.effective_message.text)
  update.message.reply_text("""
  Wrong Command.
  /help to check all supported Commands.
  """)
