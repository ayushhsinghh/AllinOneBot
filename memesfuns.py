from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
from datetime import date
from requests.structures import CaseInsensitiveDict



import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig( filename='telegram.log',
                          filemode='a',
                          datefmt='%H:%M:%S',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
   level=logging.INFO)
logger = logging.getLogger(__name__)

def get_memes():
  url = "https://api.memes.com/api/trending/feed?page=1"
  headers = CaseInsensitiveDict()
  headers["authority"] = "api.memes.com"
  headers["Content-Length"] = "0"
  headers["accept"] = "*/*"
  headers["sec-ch-ua-mobile"] = "?1"
  headers["user-agent"] = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
  headers["origin"] = "https://memes.com"
  headers["sec-fetch-site"] = "same-site"
  headers["sec-fetch-mode"] = "cors"
  headers["sec-fetch-dest"] = "empty"
  headers["referer"] = "https://memes.com/"
  headers["accept-language"] = "en-US,en;q=0.9"
  
  
  resp = requests.post(url, headers=headers).json()['posts']
  return resp


def memes(update , context):
    name = update.effective_user.first_name
    logger.info("User %s started the Memes Command.", name)
    base_url = "https://cdn.memes.com/"
    memes = get_memes()
    chat_id = update.effective_message.chat_id
    for idx , data in enumerate(memes):
      if data['mediaType'] == 1:
        img_url = base_url + data['path']
        context.bot.send_photo(chat_id=chat_id, photo=img_url)
    update.effective_message.reply_text("These Memes are From https://memes.com")
