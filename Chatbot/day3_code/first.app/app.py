from flask import Flask
import random
import requests
import bs4
from datetime import datetime as dt

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hi")
def hi():
    return "hi"

@app.route("/name")
def name():
    return "Minji Kim"

@app.route("/hello/minji")
def hello2():
    return "hello, minji"

@app.route("/hello/<person>")
def hello3(person):
    return "hello "+ person

@app.route("/cube/<num>")
def cube(num):
    result=int(num)**3
    return "{}".format(result)

#미션1 : /로또-> 랜덤한 로또 번호 추천
@app.route("/lotto")
def lotto():
    numbers=list(range(1,46))
    picks=random.sample(numbers,6)
    return str(picks)

#미션2 : /메뉴 -> 점심 메뉴 추천
@app.route("/menu")
def menu():
    menus=["햄버거","피자","치킨"]
    picks=random.choice(menus)
    return str(picks)

#미션3 : 현재 코스피 지수 띄우기
@app.route("/kospi")
def kospi():
    url="https://finance.naver.com/sise/"
    response=requests.get(url).text
    document=bs4.BeautifulSoup(response, 'html.parser')
    kkk=document.select_one("#KOSPI_now").text
    return kkk

#미션4: 새해인지 아닌지 알려주기
@app.route("/newyear")
def newyear():
    month = dt.now().month
    day = dt.now().day
    print(dt.now())
    if month == 1 and day == 1:
        return "<h1>예</h1>"
    else:
        return "<h2>아니오</h2>"

# /index
@app.route("/index")
def index():
    return "<html><head></head><body><h1>홈페이지</h1><p>이건내용</p></body></html>"
    