from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
from forex_python.converter import CurrencyRates
from newsapi import NewsApiClient
from time import sleep
from credentials import newsapikey

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename='telegram.log',
                          filemode='a',
                          datefmt='%H:%M:%S',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def tech_news(update , context):
  ''' To Get Tech News : India '''
  name = update.effective_user.first_name
  logger.info("User %s started the TechNews News.", name)
  newsapi = NewsApiClient(api_key=newsapikey)   #add NewsAPI.org Key
  tech_news =  newsapi.get_top_headlines(country="in",language="en",category="technology")
  for tech in tech_news['articles']:
    news = tech['title'] + "\n" + tech['url'] + "\n"
    update.effective_message.reply_text(news)
    sleep(0.5)
  

def trend_news(update , context):
  ''' To Get Tech News : India '''
  name = update.effective_user.first_name
  logger.info("User %s started the Trending News.", name)
  newsapi = NewsApiClient(api_key=newsapikey) #add NewsAPI.org Key
  trend_news =  newsapi.get_top_headlines(country="in",language="en")
  for trend in trend_news['articles']:
    news = trend['title'] + "\n" + trend['url'] + "\n"
    update.effective_message.reply_text(news)
    sleep(0.5)

def ent_news(update , context):
  ''' To Get Entertainment News : India '''
  name = update.effective_user.first_name
  logger.info("User %s started the Ent News.", name)
  newsapi = NewsApiClient(api_key=newsapikey) #add NewsAPI.org Key
  ent_news =  newsapi.get_top_headlines(country="in",language="en",category="entertainment")
  for ent in ent_news['articles']:
    news = ent['title'] + "\n" + ent['url'] + "\n"
    update.effective_message.reply_text(news)
    sleep(0.5)

