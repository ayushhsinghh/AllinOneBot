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


def getProfilePic(username):
  url = f"https://instadpload.herokuapp.com/profilepic?username={username}"
  resp = requests.get(url).json()
  if resp['link'] == 'Error':
      return "https://neilpatel.com/wp-content/uploads/2018/10/neilseomistake.png"
  else:
      return resp['link']


def instadp(update , context):
    name = update.effective_user.first_name
    logger.info(f"User {name} started the instadp Command with arg {context.args[0]}")
    if context.args == [] or context.args == None:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter a search term with command /instadp")
        return
    if len(context.args) > 1 or len(context.args[0]) > 15:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter a username only!")
        return
    update.effective_message.reply_text("Wait, It might take a minute")
    link = getProfilePic(context.args[0])
    chat_id = update.effective_message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=link)