from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
from forex_python.converter import CurrencyRates
from bs4 import BeautifulSoup
import os

PORT = int(os.environ.get('PORT', 5000))
token = "935149789:AAHAZbAbiumEyczdFDqM4lHo9FHd5YhRqjs"

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

def get_crypto_price():
  url = 'https://rest.coinapi.io/v1/assets?filter_asset_id=BTC;ETH;VET;XRP;LINK;DOT;QKC;TRX;WAVES;AAVE'
  headers = {'X-CoinAPI-Key' : '997D1EBE-00C6-45E8-9EE0-503AA10EF909'}
  response = requests.get(url, headers=headers).json()
  c = CurrencyRates()
  x = []
  for item in response:
    inr_rate =  c.convert('USD', 'INR', item['price_usd'])
    data = "{} : {:.2f}".format(item['name'] , inr_rate)
    x.append(data)
  return x

def get_price(update , context):
  data = get_crypto_price()
  for i in data:
    update.message.reply_text(i)

# def get_url():
#     contents = requests.get('https://random.dog/woof.json').json()    
#     url = contents['url']
#     return url

def memes(update , context):
    memes = get_memes()
    chat_id = update.message.chat_id
    for img in memes:
      context.bot.send_photo(chat_id=chat_id, photo=img)

def main():
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('memes',memes))
    dp.add_handler(CommandHandler('get_price',get_price))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=token)
    updater.bot.setWebhook('https://cybergod-telegram-bot.herokuapp.com/' + token)
    updater.idle()

if __name__ == '__main__':
    main()