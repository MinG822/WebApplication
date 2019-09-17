from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/hello/<name>")
def hello(name):
    #name에는 /hello/이름/ 활용가능 
    #템플릿 위에 파이썬 코드 결과값을 넣고 싶은 것
    return render_template('hello.html', username=name)

@app.route('/menu')
def menu():
    a="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Jajangmyeon_by_stu_spivack.jpg/240px-Jajangmyeon_by_stu_spivack.jpg"
    b="http://recipe1.ezmember.co.kr/cache/recipe/2018/08/06/db7fd75f60e162f332166a4349fcba4e.jpg"
    c="https://resources.matcha-jp.com/resize/720x2000/2017/01/20-14267.jpeg"
    menu={"짜장면":a, "호떡":b, "스시":c}
    pick=random.choice(list(menu.keys()))
    #랜덤으로 음식 메뉴를 추천하고
    #해당음식사진을 보여주는 기능을 구현g
    return render_template('menu.html', name=pick, image=menu[pick])

#/lotto 랜덤 넘버를 추천해주고, 최신 로또와 비교하여 등수를 알려주는 기능
@app.route("/lotto")
def lotto():
    yourlotto = sorted(random.sample(range(1,46),6))
    url="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    response = requests.get(url)
    lotto_dict = response.json()
    
    winner=[]
    for i in range(1,7):
        winner.append(lotto_dict["drwtNo{}".format(i)])
    
    count=len(set(winner)&set(yourlotto))
    return render_template('lotto.html', Lotto= winner, Yourlotto=yourlotto, Count=(7-count))



if __name__ == "__main__":
    app.run(debug=True) 