import requests
from forex_python.converter import CurrencyRates
from credentials import coinAPIio

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename='telegram.log',
                          filemode='a',
                          datefmt='%H:%M:%S',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def get_crypto_price():
  url = 'https://rest.coinapi.io/v1/assets?filter_asset_id=BTC;ETH;VET;XRP;LINK;DOT;QKC;TRX;BAND;LTC;ZIL;BNB;SC;BZRX;GAS;AMB;WRX;BLZ;MATIC'
  headers = {'X-CoinAPI-Key' : coinAPIio}   #add coinAPI.io API Key
  response = requests.get(url, headers=headers).json()
  c = CurrencyRates()
  x = []
  for item in response:
    inr_rate =  c.convert('USD', 'INR', item['price_usd'])
    data = "{} : {:.2f}".format(item['name'] , inr_rate)
    x.append(data)
  return x


def crypto_price(update , context):
  name = update.effective_user.first_name
  logger.info("User %s started the crypto_price Command.", name)
  data = get_crypto_price()
  for i in data:
    update.effective_message.reply_text(i)