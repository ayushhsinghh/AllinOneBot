import requests
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename='telegram.log',
                          filemode='a',
                          datefmt='%H:%M:%S',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


''' 
Function to get Links for Paid Udemy course that are free now.
This backend API is hosted on heroku. Don't overuse it.
'''
def free_udemy_coupon(update , context):
  name = update.effective_user.first_name
  chat_id = update.message.chat_id
  logger.info(f"User {name}:{chat_id} started the Udemy Coupon Command.")
  res = requests.get("https://freeudemycourse.herokuapp.com/").json()
  for idx , data in enumerate(res):
    update.effective_message.reply_text(f"{idx + 1}: {data['Name']} : {data['Link']}")
    
    