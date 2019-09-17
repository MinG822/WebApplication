from flask import Flask, render_template, request
import requests
from pprint import pprint
from decouple import config
import random
from bs4 import BeautifulSoup
#예쁘게 출력하는 코드

#토큰은 집열쇠같은 것인데, 나중에 아마존웹서비스같은 곳에 올려두었다가 뺏기면 권한을 다 넘겨주게된다
#얘를 어떻게 숨겨야될까, 컴퓨터에만 숨겨두는게 좋다
#첫번째는 os단계에서 숨겨두기, 환경변수에다가.
token = config("TELEGRAM_TOKEN")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result():
    base = "https://api.telegram.org"
# chat_id를 가져오는 코드
#1. getUpdates 메소드로 요청 보내기
#2. 받아온 응답(json)을 딕셔너리로 바꿔서 타겟하는 목표물인 아이디를 가져오기
    method2 = "getUpdates"
    url2= f"{base}/bot{token}/{method2}"
    response=requests.get(url2)
    res =response.json()
    chatid = res["result"][0]["message"]['from']['id']
    method = "sendMessage"
    text= request.args.get('txt')
    # interpolation을 하면 이쁘고 깔끔하다
    url=f"{base}/bot{token}/{method}?chat_id={chatid}&text={text}"
    requests.get(url)

    return render_template('result.html', text=text)

@app.route(f'/{token}', methods=['POST'])
def webhook():
    #1. 메아리 챗봇
    # 웹훅을 통해 텔레그램 보낸 요청안에 있는 메시지를 가져와
    # 그대로 전송
    res = request.get_json()
    
    text = res.get('message').get('text')
    chat_id = res.get('message').get('chat').get('id')
    
    base = "https://api.telegram.org"
    method = "sendMessage"
    

    if res.get('message').get('photo')[-1].get('file_id') is not None:
    # 만약 이 값이 있다면 이프문 실행, 아니면 none이 반환될 것이다. 더 명확하게 is not None: 을 붙여도된다.
        file_id = res.get('message').get('photo')[-1].get('file_id')
        file_res = requests.get(f'{base}/bot{token}/getFile?file_id={file_id}')
        file_path = file_res.json().get("result").get("file_path")
        file_url=f'{base}/file/bot{token}/{file_path}'
        image=requests.get(file_url, stream=True)
        # 요청지의 주소에는 파일스트림, 파일이 있을 것이다라고 명확히 알려줌
        url = "https://openapi.naver.com/v1/vision/celebrity"
        client_id = config('NAVER_ID')
        client_secret = config('NAVER_PSSWD')
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        files = {'image': image.raw.read()}
        #우리이미지파일을 날것으로 받아서 읽어라
        clova_res = requests.post(url, files=files, headers=headers)
        text =clova_res.json().get('faces')[0].get('celebrity').get('value')
        howmuch = clova_res.json().get('faces')[0].get('celebrity').get('confidence')
        roundhowmuch = round(howmuch,2)
    # else : 


    # for i in ["lotto","Lotto","로또"]:
    #     if  i in text:
    #         text= str(sorted(random.sample(range(1,46),6)))
    
    # if text == "kospi":
    #     url2="https://finance.naver.com/sise/"
    #     response = requests.get(url2).text
    #     docu=BeautifulSoup(response,'html.parser')
    #     kos = docu.select_one("#KOSPI_now").text
    #     text = str(kos)
    

    # elif text[0:3] == "/번역":
    #     ## papago로 번역 결과를 뽑아오면 된다
    #     papaurl = "https://openapi.naver.com/v1/papago/n2mt"

    #     headers = {
    #       'X-Naver-Client-Id':config('NAVER_ID'),'X-Naver-Client-Secret':config('NAVER_PSSWD')
    #     }

    #     data = {
    #       'source' : 'ko', 'target' : 'en', 'text' : f"{text[3:]}"
    #     }

    #     res = requests.post(papaurl, headers=headers, data=data)
    #     text=res.json().get("message").get('result').get('translatedText')


    url = f"{base}/bot{token}/{method}?chat_id={chat_id}&text={roundhowmuch*100}%로 {text}를 닮았습니다!"
    requests.get(url)

    # 사용자가 입력한 값들이 프린트 될 것이다.
    return '',200

if __name__ == "__main__":
    app.run(debug=True)