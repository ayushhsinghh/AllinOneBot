import requests
from bs4 import BeautifulSoup
import json
import re

session = requests.Session()
headers = {
    'authority': 'maps.googleapis.com',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
    'accept': '*/*',
    'referer': 'https://www.real.discount/',
    'accept-language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
    'Origin': 'https://www.real.discount',
    'origin': 'https://www.real.discount',
    'content-length': '0',
    'content-type': 'text/plain',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}
response = session.get('https://www.real.discount/udemy-coupon-code/', headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

extra_headers = {
    'authority': 'www.google-analytics.com',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
    'accept': '*/*',
    'referer': 'https://app.real.discount/',
    'accept-language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
    'Origin': 'https://app.real.discount',
    'origin': 'https://app.real.discount',
  }
divElement = soup.find_all("div", {"class": "col-lg-4 col-md-6"})
name = [ num.find_all('h5' , {"class": "mt-0"})[0].get_text()  for idx , num in enumerate(divElement) ]
description = [ num.find_all("p", {"class": "mb-5"})[0].get_text()  for idx , num in enumerate(divElement) ]
imgURL = [ data.find_all('img')[0].get("src")  for idx , data in enumerate(divElement) ]
urlList = [(divElement[idx].find_all("a")[0].get("href")) for idx , num in enumerate(divElement)]
udemyURL = []
for idx , num in enumerate(urlList):
  response1 = session.get(num, headers=extra_headers)
  soup1 = BeautifulSoup(response1.content, 'html.parser')
  udemyURL.append(soup1.find_all('a', {'href': re.compile(r'udemy\.com/')})[0].get("href"))


result  = [{'Description': desc, 'Name' : name , 'Thumbnail': img, 'Link': link} for desc,name,img,link in zip(description,name,imgURL,udemyURL)]
json_object = json.dumps(result, indent = 3) 

print(json_object)


