from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from credentials import token 
from Newsfun import *
from helperCommand import *
from memesfuns import get_memes , memes
from torrent import torrent
from udemyCoupon import free_udemy_coupon
from cryptoPrice import get_crypto_price , crypto_price
from vaccineUpdate import vaccineUpdate , vaccineUpdatedelhi
from wheretoWatch import whereToWatch
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    InlineQueryHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

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
    dp.add_handler(MessageHandler(Filters.regex('^.*(torrent).*$') & ~Filters.command, torrentError))
    dp.add_handler(MessageHandler(Filters.regex('^.*(where).*$') & ~Filters.command, watchError))
    dp.add_handler(CommandHandler('trend_news',trend_news))
    dp.add_handler(CommandHandler('torrent' , torrent))
    dp.add_handler(CommandHandler('wheretowatch' , whereToWatch))
    dp.add_handler(CommandHandler('udemycoupon',free_udemy_coupon))
    dp.add_handler(CommandHandler('crypto_price',crypto_price))
    dp.add_handler(MessageHandler(Filters.command, wrongCommend))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


