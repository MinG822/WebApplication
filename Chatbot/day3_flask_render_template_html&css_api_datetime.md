# Start Camp (3rd day)

- GIT hub에서 포폴을 관리하자
  - **TIL(Today I learned)**
    : 매일 배운 것을 정리하고 업로드하는 프로젝트
    : 인터넷에 TIL을 치면 다른 사람들의 예시들을 볼 수 있다.
- 지저분한 파일관리
    : 일별로 끊어도된다.
    : git에서 파일을 이동시킬 때 : mv 파일명 폴더명/
  
- Khan Academy?
  : 오픈 온라인 강의 사이트(중고등학교 교육과정)

- **개발자가 성장하기 위한 커리어?**
  : 중견기업이나 스타트업에서 시작하는 것이 좋다
  : 대기업에 들어가면 아주 작은 파트만 맡게 된다
  : 개발자의 커리어는 변화가능성이 무궁무진하다
  : 그러니 선택의 폭을 넓혀서 생각하자
  : programmers를 이용하자!
  
- **programmers**
  : 코드 중심의 프로그래머 채용 서비스
  : 이화경 대표(네이버와 카카오 CTO)
  : 좋은 개발자와 좋은 업체 매칭을 도와준다
  : **처음에는 최소 50억이상 투자 받은 회사만 가자** 
  : 코딩테스트 연습도 있다!
  
- y combinator
  : 스타트업계의 할리우드
  
- 개발자란?
  : 프로젝트를 처음부터 끝까지 맡아서 끝낼 수 있는 사람
  : 프로젝트란 실용적인 서비스를 만들어내는 것
  
- **mvp(minimum viable program)** 
  : 최소 기능을 하는 프로그램을 만들어내는 것
  : 소프트웨어 업계에서 가장 중요
  : 완결성 있는 제품을 만들어내야하는 제조업과 달리 소프트웨어는 매우 유연하며 처음 슈팅되는 제품이 완성된 모습일 필요가 없다.
  : 중요한 건 속도. 가장 빠르게 고객의 니즈에 맞게 변화시킬 수 있는 가가 관건
  : 예를 들어서 토스는 개발주기가 2주, 즉 2주마다 업데이트가 됨
  
- 버클리 software engineering (cs 169)
  : edex에서 이용가능(saas)(agile development using ruby on rails)
  : ssafy 수업 빌딩에 큰 영향
  : 데이빗 패터슨의 강의
  : 소프트웨어라는 것이 뭔지 전달하는 수업
  : 단점, 수업 양이 방대하다

  

---

## 1. flask를 이용한 앱 구현

_flask 주소 : http://flask.pocoo.org/_

- flask의 홈페이지에 있는 코드를 가져오면 매우 간단하게 서버가 되어 서비스를 만들고 url을 통해 클라이언트의 요구에 응답할 수 있다.

  ```
  from flask import Flask
  app = Flask(__name__)
  
  @app.route("/")
  def hello():
      return "Hello World!"
  ```

  - 실습에서 만든 사이트는 이용자가 나밖에 없지만, 만약 클라우드 서버에 업로드하면 다른 사람도 이용가능하다.
  - 구동은 gitbash flask run 으로, 코드 변경시마다 재구동해야한다)
  - git bash에 flask run을 치면 웹주소(http://127.0.0.1:5000/)가 하나 나오고 코드에서 구현한 내용이나온다. 이때 항상 파일이름이 app.py여야한다.



- 서비스를 만드는 것 == 주문서 만드는 것 

  - 주문서는 1. 어떻게 주문할지, 2. 무엇을 제공할지가 들어가 있어야한다.

  -  flask 의 코드에서 1번은 @app.route("/"), 2번은 def hello(): return "Hello World!" 이다.

    

  1. **주문서를 받는 방법** 

     - "/"을 바꿔주면 된다.
     - /의 절대적인 의미는?  루트!
     -  ex) 깃배쉬에서 / 라고 치면 가장 상위에 있는 위치(루트)가 나온다

  2. **주문서를 만드는 작업 (라우팅)** 

     ```python
     #변수를 사용하지 않는 경직된 방식
     
     @app.route("/hi")
     def hi():
         return "hi"
     # http://127.0.0.1:5000/hi에 접속하면 -> hi가 나오게된다.
     
     @app.route("/name")
     def name():
         return "Minji Kim"
     
     @app.route("/hello/minji")
     def hello2():
         return "hello, minji"
     
     #변수를 사용하는 배리어블 라우팅
     
     @app.route("/hello/<person>")
     def hello3(person):
         #return "hello "+ person
     	#return f"hello{}".person
     	#return "hello{}".format(person)
     	#return "hello" + str(person)
         
     @app.route("/cube/<num>")
     def cube(num):
         result=int(num)**3
         return "{}".format(result)
     ```

     - 변수를 만드는 방법
       : 꺽쇠를 만들면 변수, 꺽수안에 이름을 집어넣기
       : 파이썬 코드에서 이 변수이름으로 변수를 똑같이 활용가능
       : 사용자가 요청한 바를 변수로 만들어 주문서를 만들 수 있다.

     - 입력된 값은 str이기 때문에 수리계산을 위해서는 항상 int 변환을 해야한다.  
       : 그렇지 않았을 때 나오는 에러(사이트와 깃배쉬)
       Internal Server Error

       The server encountered an internal error and was unable to complete  your request. Either the server is overloaded or there is an error in  the application.

       TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

       

     - return 값이 string, dict, tuple 중에 하나여야 한다.
       :그렇지 않을 경우 나오는 
       TypeError: The view function did not return a valid response. The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a int.
       
     - 프린트함수로는 브라우저에 띄울수 없기 때문에 항상 리턴만 이용해야함
       
     - 출력하고 싶을 땐 머스태치 {{}} 사용
       
       

- **flask Mission**

  ```python
  import random
  import requests
  import bs4
  from datetime import datetime as dt
  
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
  # <h1></h1> 등은 html(HyperText Markup Language)의 문법이다. 마크업 하는 것
  ```

  

- **datetime 패키지**
  : 날짜시간 정보를 가져와주는 패키지

  - 클래스와 메서드
  :  datetime에는 datetime, weekday, strftime와 같은 클래스가 있음, ex)datetime.datetime
    : 클래스에서는 객체 생성하지 않고도 바로 클래스에서 사용할 수 있는 클래스 메서드를 제공한다. 
  : datetime.datetime 클래스의 메서드 표
  
  |   메서드   | 설명                                                         |
  | :--------: | :----------------------------------------------------------- |
  |   now()    | 컴퓨터 현재 시간을 datetime.datetime클래스 객체로 만들어 반환한다. <br />속성: year, month, day, hour, minute, second, microsecond(백만분의일초) 등 |
  | weekday()  | 요일을 딕셔너리 자료형으로 반환                              |
  |   date()   | 날짜 정보만 가지는 datetime.date 클래스 객체를 반환한다      |
  |   time()   | 시간 정보만 가지는 datetime.time 클래스 객체 반환            |
  | strftime() | 정보를 문자열로 반환                                         |
  
    ex) datetime.datetime.now().year
  
- **파이썬 코드 안에 html파일을 만들어보자!**

  ```python
  # /index
  @app.route("/index")
  def index():
      return "<html><head></head><body><h1>홈페이지</h1><p>이건내용</p></body></html>"
  ```


   : 불편하기 때문에 html파일을 만들어 flask의 render_template()를 통해 그 파일을 가져오게 만들어 보자.

---



## 2. html과 css 기본기본 문법

- 브라우저라는 것은 html(과 css)로 만들어진 파일을 형식에 맞춰 보여주는 것
- html은 뼈대이고 css (cascading style sheet)는 꾸미기역할. 근데 어렵다...

- 실습 코드

```html
<!DOCTYPE html>
<html>
    <head>
        <title>HomePage</title>
    </head>
    <body style="background-color: cadetblue">
        <h1 style="color:rgb(2, 47, 68)">It is Minji's</h1>
        <h2>Welcome</h2>
        <h3>Thank you for visiting </h3>
        <p>I'm studying programming at SSafy</p>
        <p>I downloaded live server</p>
        <a href="http://www.google.com">a means anker to go somewhere:here it is google</a>
        <ul>
            <li>cat</li>
            <li>lovely cat</li>
            <li>cat is everything</li>
        </ul>
        <ol>
            <li>studying at SSAFY</li>
            <li>is hell</li>
            <li>nine to six</li>
        </ol>
        <img width="400" height="400" src="https://upload.wikimedia.org/wikipedia/commons/6/66/An_up-close_picture_of_a_curious_male_domestic_shorthair_tabby_cat.jpg">
        <iframe width="400" height="400" src="https://www.youtube.com/embed/5dsGWM5XGdg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </body>
</html>
```

- 자동 리로드 방법 
  : Live Server extension 설치하기-> open with Live Server
  : flask에는 적용되지 않음

- <head><title> 은 탭의 이름

- <a></a>는 링크를 걸어주는 역할(anker)
  : a href ="http address"
  : href(hyper reference)는 a의 속성이다. 
  : http를 안붙이면 로컬로부터 가져온다. (http://127.0.0.1:5500/homepage/www.google.com)

- <img>는 이미지를 불러오는 역할
  : src source="주소"(주소는 컴퓨터로부터 가져올 수도, 인터넷에서 가져올 수도 있다)
  : 단위는 픽셀단위이며 상대값

- < iframe> 은 동영상을 불러오는 역할
  : youtube의 공유의 iframe을 그대로 복사해오면된다.
  :동영상마다 설정이달라서 외부에선 아예돌아가지 않는 경우도 있다.

- ul은 unordered list

- ol은 ordered list 
  :숫자인덱스를 스타일링하기 어려우니 ol을 잘 안쓰긴 한다.
  
- style(css문법)
  : 해당 내용물의 색깔 등을 지정해 줄 수 있다
  
- !하고 tab을 누르면 기본 코드를 자동완성 시켜주는 스크립트

---



## 3. flask의 render_template 이용하기

- render_template()는 flask에서 지원하는 함수. import해주기
  : render_template('html주소', html파일에서 사용할 변수명=app.py에서 사용한 변수명)

- api를 통해 당첨로또 정보를 가져오기 위해서 2차시의 requests함수를 이용

  - 스크래핑과 api는 비슷한 동작원리
  - api용 파서 : request.json()
    : 요청해서 응답받을 때 스크래핑은 html으로 받지만, api는 json의 keyvalue파일로 받음. 
    : request.json() 은 파이썬은 이를 글자로만 인식하기 때문에 딕셔너리로 인식케함

- 로또 여러 기능을 구현한 파이썬 코드 

  - api로 로또 번호 가져오기

    ```python
    # lotto api를 통해 최신 당첨 번호를 가져온다.
    
    import requests
    import random
    
    url="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    requests.get(url)
    response = requests.get(url)
    # json파일을 파이썬 딕셔너리로 바꿈
    dict_lotto = response.json()
    
    #로또 당첨 번호알려주기
    winner=[]
    for i in range(1,7):
        winner.append(dict_lotto["drwtNo{}".format(i)])
    
    print("당첨번호는 {}입니다.".format(winner))
    ```

  - 로또 당첨여부알려주기

    ```python
    # 로또 당첨 여부 알려주기
    your_lotto = sorted(random.sample(range(1,46),6))
    count=0
    # 방법1
    for i in winner:
        for j in your_lotto:
            if i==j:
                count=+1
                break
    # 방법2 : 교집합의 길이를 재주는 코드. 이러면 for 문을 쓸 필요가 없다.
    count = len(set(winner) & set(your_lotto))
    
    print ("{}등 당첨입니다! 축하드려요!".format(7-count))
    ```

  - 로또가 당첨될 때 까지

    ```python
    # 몇 번 째에 로또가 당첨되었는지를 알려주는 코드
    count2=0
    while True:
        count2+=1
        your_lotto = sorted(random.sample(range(1,46),6))
        if your_lotto == winner:
            break
    
    print("당신의 로또는 {}입니다.".format(your_lotto))
    print("{}회차에 당첨되셨습니다. 당첨금은 {}이고 비용은 {}원입니다. 총 {}를 획득하셨어요! 수고하셨습니다!".format(count2, 1868470000, count2*5000, 1868470000-count2*5000))
    ```

    

- 최종 파일

```python
from flask import Flask, render_template
import random
import requests 

app = Flask(__name__)

# 홈페이지
@app.route("/")
def home():
    return render_template('home.html')

#name에는 /hello/이름/ 변수로 활용가능 
#템플릿 위에 파이썬 코드 결과값을 넣고 싶은 것

@app.route("/hello/<name>")
def hello(name):
    return render_template('hello.html', username=name)

#랜덤으로 음식 메뉴를 추천하고
#해당음식사진을 보여주는 기능을 구현
@app.route('/menu')
def menu():
    a="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Jajangmyeon_by_stu_spivack.jpg/240px-Jajangmyeon_by_stu_spivack.jpg"
    b="http://recipe1.ezmember.co.kr/cache/recipe/2018/08/06/db7fd75f60e162f332166a4349fcba4e.jpg"
    c="https://resources.matcha-jp.com/resize/720x2000/2017/01/20-14267.jpeg"
    menu={"짜장면":a, "호떡":b, "스시":c}
    pick=random.choice(list(menu.keys()))

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


# 자동으로 서버가 리로드 되는 방법 
if __name__ == "__main__":
    app.run(debug=True) 
# +앱돌리듯이 git bash python app.py
```

- templates의 html파일들 내용
  : flask.render_template("html주소")함수를 쓸 때는 반드시 html파일들이 templates 폴더 안에 들어있어야한다.(설정을 바꾸지 않는 한)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    #home.html 파일의 바디내용
    <h1>Home Page</h1>
    
    #hello.html 파일의 바디내용
    <h1>Hello {{username}} </h1>
    
    #menu.html 파일의 바디내용
    <h1> {{name}} </h1>
    <img src = "{{image}}">
    
    #lotto.html 파일의 바디내용
       <h1>로또 당첨 확인 페이지입니다 </h1>
    <p>이번회차 로또는 {{Lotto}}입니다.</p>
    <p>당신의 로또는 {{Yourlotto}}입니다.</p>
    <p>축하합니다. {{Count}}등에 당첨되셨습니다. (6등부터는 꽝입니다.)</p>
    
</body>
</html>
```



---



## + 주문서

http://naver.com:80/

네트워크들어가면 헤더에서 주문서의 정보들이 나온다

1. http://
   : hyper text transfer protocol
   : 정보(101010..)를 주고 받는 방식(protocol, 일종의 약속), 

2. 원격지 주소(IP)
    : 210.89.164.90:443 

3. naver.com
   :원격지 주소에 이름을 붙인 것, 더 쉽다. 도메인,  top level domain(TLD)

4. :80
   : 정보가 들어오는 기본 대문, http의 대문이다. 
   22번 포트 : 시큐어설 포트, 카페주인만들어가는 문
   80번 포트  : 고객들이 들어가는 문

5. /
   : 루트, 뒤에 다른 페이지가 붙는데 이게 상세주문



---

## +오늘의 git bash 명령어

- cd ~(물결모양)  홈폴더로 이동한다

- flask run이후 ctr+ c를 누르면 명령어 입력모드로 변환

- *는 모든 객체를 의미한다





