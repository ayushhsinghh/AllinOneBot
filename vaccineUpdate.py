import requests
import logging
from datetime import date

'''
For Changing City

Just Change To CityID in jsonresdis

eg. For Delhi CityID is 141..

jsonresdis = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=141&date={today}").json()

change : district_id=141 in URI



'''


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename='telegram.log',
                          filemode='a',
                          datefmt='%H:%M:%S',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def vaccineUpdate(update , context):
  ''' It is For Varanasi Only '''

  name = update.effective_user.first_name
  logger.info("User %s started Vaccine Update Varanasi", name)
  user = update.effective_message.from_user
  logger.info("User %s started the Vaccine Update Varanasi.", user.id)
  today = date.today().strftime("%d-%m-%Y")
  jsonresdis = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=696&date={today}" , headers = headers).json()

  for i in range(len(jsonresdis["centers"])):
    if jsonresdis["centers"][i]["sessions"][0]["min_age_limit"] == 18:
      hos_name = jsonresdis["centers"][i]["name"]
      avail_vaccine = jsonresdis["centers"][i]["sessions"][0]["available_capacity"]
      sessionlen = len(jsonresdis["centers"][i]["sessions"])
      if sessionlen > 0:
        for j in range(len(jsonresdis["centers"][i]["sessions"])):
          if jsonresdis["centers"][i]["sessions"][j]["available_capacity"] > 0:
            avail_vaccine = jsonresdis["centers"][i]["sessions"][j]["available_capacity"]
            hos_name = jsonresdis["centers"][i]["name"]
            vdate = jsonresdis["centers"][i]["sessions"][j]["date"]
            y = f"{hos_name} : {avail_vaccine} Vaccine Available on {vdate}"
            update.effective_message.reply_text(y)
      else:
        x = f"{hos_name} : {avail_vaccine} Vaccine Available"
        update.effective_message.reply_text(x)

def vaccineUpdatedelhi(update , context):
  name = update.effective_user.first_name
  logger.info("User %s started Vaccine Update Delhi", name)
  today = date.today().strftime("%d-%m-%Y")
  jsonresdis = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=141&date={today}" , headers = headers).json()
  for i in range(len(jsonresdis["centers"])):
    if jsonresdis["centers"][i]["sessions"][0]["min_age_limit"] == 18:
      hos_name = jsonresdis["centers"][i]["name"]
      avail_vaccine = jsonresdis["centers"][i]["sessions"][0]["available_capacity"]
      sessionlen = len(jsonresdis["centers"][i]["sessions"])
      if sessionlen > 0:
        for j in range(len(jsonresdis["centers"][i]["sessions"])):
          if jsonresdis["centers"][i]["sessions"][j]["available_capacity"] > 0:
            avail_vaccine = jsonresdis["centers"][i]["sessions"][j]["available_capacity"]
            hos_name = jsonresdis["centers"][i]["name"]
            vdate = jsonresdis["centers"][i]["sessions"][j]["date"]
            y = f"{hos_name} : {avail_vaccine} Vaccine Available on {vdate}"
            update.effective_message.reply_text(y)
      else:
        x = f"{hos_name} : {avail_vaccine} Vaccine Available"
        update.effective_message.reply_text(x)

