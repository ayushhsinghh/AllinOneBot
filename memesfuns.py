from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
from bs4 import BeautifulSoup
from datetime import date
from Newsfun import *


import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig( filename='telegram.log',
                          filemode='a',
                          datefmt='%H:%M:%S',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
   level=logging.INFO)
logger = logging.getLogger(__name__)

def get_memes():
  session = requests.Session()
  response = session.get("https://memechat.app")
  soup = BeautifulSoup(response.content, 'html.parser')
  content_class =  soup.find_all("div", {"class": "article-content"})
  images = []
  image_url = []
  i = 0
  for img in content_class:
    images.append( img.find_all('img'))
    image_url.append(images[i][0]['src'])
    i = i + 1
  return image_url


def memes(update , context):
    name = update.effective_user.first_name
    logger.info("User %s started the Memes Command.", name)
    memes = get_memes()
    chat_id = update.effective_message.chat_id
    for img in memes:
      context.bot.send_photo(chat_id=chat_id, photo=img)