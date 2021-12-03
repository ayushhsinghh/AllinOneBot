import requests
from bs4 import BeautifulSoup
import urllib.parse

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename='telegram.log',
                          filemode='a',
                          datefmt='%H:%M:%S',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def torrent(update , context):
  user_says = " ".join(context.args)
  name = update.effective_user.first_name
  chat_id = update.message.chat_id
  logger.info(f"User {name}:{chat_id} started the torrentDownload with Argument '{user_says}'")

  mess = f'Wait, Searching PirateBay : {user_says}'
  update.effective_message.reply_text(mess)
  encoded = urllib.parse.quote(user_says)
  url = f'https://torrentmagnetdownloader.herokuapp.com/?search={encoded}'
  result = requests.get()
  for info in result:
    update.message.reply_text(info)