import requests
from bs4 import BeautifulSoup
from decouple import config

base = "https://api.telegram.org/"
token = config("TELEGRAM_TOKEN")
method = "sendMessage"
chatid="789987742"
text="몽총몽총"
url=base+'bot'+token+method+"?"+"chat_id="+chatid+"&text="+text

response=requests.get(url)
print(response)


