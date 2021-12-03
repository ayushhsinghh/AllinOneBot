import requests
import logging
import urllib.parse


logging.basicConfig(filename='telegram.log',
                          filemode='a',
                          datefmt='%H:%M:%S',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


''' 
Function to get torrent Magnet links
'''


def torrent(update , context):
  user_says = " ".join(context.args)
  if user_says == "":
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter a search term with command /torrent")
    return
  name = update.effective_user.first_name
  chat_id = update.message.chat_id
  logger.info(f"User {name}:{chat_id} started the torrentDownload with Argument '{user_says}'")

  mess = f'Wait, Searching PirateBay : {user_says}'
  update.effective_message.reply_text(mess)
  encoded = urllib.parse.quote(user_says)
  url = f'https://torrentmagnetdownloader.herokuapp.com/?search={encoded}'
  result = requests.get(url).json()
  if len(result) == 0:
    update.message.reply_text('Sorry No result Found')
  else:
    for idx,data in enumerate(result):
      update.message.reply_text(f"{idx + 1}: { data['name'] }\n{data['size']}")
      update.message.reply_text(data['magnet'])