import requests
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import urllib3

logging.basicConfig(filename='telegram.log',
                          filemode='a',
                          datefmt='%H:%M:%S',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


''' 
This Function returns all provider where this Movie/show is Found.
This backend API is hosted on heroku. Don't overuse it.
'''
def whereToWatch(update , context):
  name = update.effective_user.first_name
  chat_id = update.message.chat_id
  user_says = " ".join(context.args)
  if user_says == "":
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter a search term with command /torrent")
    return
  
  logger.info(f"User {name}:{chat_id} started the Udemy Coupon Command.")
  encoded = urllib3.parse.quote(user_says)
  url = f'https://wheretowatch.herokuapp.com/{encoded}'
  result = requests.get(url).json()
  if len(result) == 0:
    update.message.reply_text('Sorry No result Found')
  else:
    for idx,data in enumerate(result):
      update.message.reply_text(f"{idx + 1}: {data['title']}\ntype: {data['Content Type']}")
      update.message.reply_text(data['Poster'])
      for link in data['Providers']:
          update.message.reply_text(link)
      
    