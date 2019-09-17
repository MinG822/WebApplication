from flask import Flask, render_template, request
from faker import Faker
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)
fake = Faker('ko_KR')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pastlife')
def pastlife():
  
    
    return render_template('pastlife.html')

baitdict={}
# 딕셔너리를 전역변수로 설정해야 페이지에 들어갈 때마다 딕셔너리가 새롭게 리로드되는일이없다

@app.route('/result')
def result():
    # 전생으로 활용할 직업들을 만들어주는 faker라는 패키지를 활용
    # 이름과 (가짜) 직업을 알려준다.
    
    Job = fake.job()
    Name =request.args.get('id')
    #requests와 완전다르다. flask의 함수
    #return render_template('result.html', Job=jobdict[Name], name=Name)

    #만약 한번 나온 결과는 그대로 유지하려면? hint 딕셔너리 사용
    #1.우리 데이터에 해당하는 이름이 있는지 없는지 확인
    if Name not in baitdict.keys():
        baitdict[Name]=Job
        return render_template('result.html', job=Job, name=Name)
    else:
        Job = baitdict[Name]
        return render_template('result.html', job=Job, name=Name)

#dictionary.keys()로 반환된 자료형은 dictionary keys 자료형. 리스트로 변환가능하다

@app.route('/goonghab')
def goonghab():
    return render_template('goonghab.html')

v_dict={}
babos={}

@app.route('/destiny')
def destiny():
    v=random.choice(range(51,101))
    babo= request.args.get('babo')
    idol= request.args.get('idol')
## 미션 babo와 ido의 궁합값을 저장해두고 같은 입력값이 있을 때는 그 값을 가져오기
# 내 답
    # if ((babo,idol) in v_dict.keys()):
    #     v= v_dict[(babo,idol)]
    # elif ((idol,babo) in v_dict.keys()):
    #     v=v_dict.keys[(idol,babo)]
    # else:
    #     v_dict[(babo,idol)]=v

## 선생님 답 : 딕셔너리 안에 딕셔너리를 집어넣기
    # babos= {
    #     babo : {
    #         idol : v
    # #     }
    # # }

    if babo in babos.keys():
        if idol in babos[babo].keys():
            v= babos[babo][idol]
        # 키의 경우라면 키 in 딕셔너리 로도 충분하다
        else:
            babos[babo][idol]=v
    elif idol in babos.keys():
        if babo in babos[idol].keys():
            v= babos[idol][babo]
        else:
            babos[idol][babo]=v
    else : 
        babos[babo]={idol:v}
        babos[idol]={babo:v}
    return render_template('destiny.html', V=v, babo=babo, idol=idol)

babos_list=[]
#babos 에 있는 사람들을 모두 출력하기
#어떻게 예쁘게 출력하지??
@app.route('/admin')
def showem():
    for k,v in babos.items():
        babos_list.append((k,v))
    
    return render_template('showem.html',babobabo=babos_list)

@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/search')
def search():
    name =request.args.get('userName')
    url="https://www.op.gg/summoner/userName={}".format(name)
    response=requests.get(url).text
    document=BeautifulSoup(response, 'html.parser')
    win=document.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins').text
    lose=document.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses').text
    win=win.replace('W','')
    lose=lose[:3]
    return render_template('search.html',win=win,lose=lose,name=name)

if __name__ == "__main__" :
    app.run(debug=True)