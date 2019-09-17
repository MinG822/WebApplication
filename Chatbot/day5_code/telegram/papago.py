import requests
from decouple import config
from pprint import pprint

url = "https://openapi.naver.com/v1/papago/n2mt"

headers = {
    'X-Naver-Client-Id':config('NAVER_ID'),
    'X-Naver-Client-Secret':config('NAVER_PSSWD')
}

data = {
    'source' : 'ko',
    'target' : 'en',
    'text' : "띠용"
}

res = requests.post(url, headers=headers, data=data)
pprint(res.json())
#이건 get과 달리 보내주는것!