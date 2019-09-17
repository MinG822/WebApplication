# Start Camp Chatbot (4st day)

-  **static page**
  - 컨텐츠의 변화없이 누가들어와도 동일한 컨텐츠를 제공하는 사이트
  - 회사 소개 홈페이지, 개인 포폴 페이지 등
  - 서비스를 fully 제공하기 어려움
- **Dynamic page**
  - 사용자들의 요청에 따라 여러 컨텐츠를 동적으로 변화시켜서 주는 사이트
  - 정적 페이지를 웹에 배포해보기(git hub를 통해서)(쌤이 안하셨다!)
-  다이나믹 페이지는 웹에 배포하기 어려워서 아직 하지 않음.
-  어제했던 페이지에서 시작, 인터랙티브하게 변화를 주기
- 그러기 위해서는 사용자의 입력값을 우리가 처리할 수 있어야한다.

---



## 0. Outline

_4차시에 실습해본 서비스의 간략한 개요_

- 구조: 1. app.py 2.templates의 html파일들

- 작동방식 : app.py에서는 라우팅작업들을 해주고 결과는 templates의 html파일들로 연결해 출력
  - 필요한 기능 
    1. app.py에서 설정한 변수들을 html파일에 전달
       :  render_template('html주소', html변수=app.py변수 )
    2. html에서 사용자에게 입력받은 값을 app.py에 전달
       - form, input, button 태그: 사용자로부터 입력값 전달받기
       - flask의 request.args.get('input의 name속성값'): 입력값 app.py에 전달하기

- 구현할 서비스

  1. 가짜 구글 & 검색엔진 모음 
     - 사용자 입력값의 구글, 네이버, 다음 검색 결과 페이지로 연결
  2. 전생의 직업
     - fake 패키지로 직업 랜덤 검색(+한국어설정)
     - 검색한 이름과 나온 랜덤 직업을 딕셔너리에 저장해 재 검색시 같은 결과 출력하기
  3. 궁합 보기
     - randint(시작값, 끝값)으로 랜덤 값 출력
     - 결과를 저장하기 위해 이중 딕셔너리 사용
     - 내 이름과 상대방 이름의 순서를 바꾸어도 같은 결과 값이 나오도록 if문 활용
     - showem.html을 만들어 저장된 결과 값들 출력
  4. 롤 계정 승패 확인
     - 사용자의 계정을 입력받아
     - 롤 홈페이지에서 해당 계정의 승패 값 스크래핑하고
     - 그 결과를 출력하기

  _모든 서비스는 홈페이지에서 연결되게 설정!_

---



## 1. 가짜 구글 & 검색엔진모음 

- 가짜 구글 페이지 작동 방식

  - 사용자로부터 입력값을 받았을 때, 구글에서 그 입력 값으로 검색한 페이지로 연결해주기

- 입력값 받는 법 

  - input
    - 사용자의 입력값을 받게 해주는 태그
    - name 속성은 사용자의 입력값을 저장하고 있는 변수의 이름을 지정하는 역할
  - buttom
    - 버튼이 없을 때는 엔터를 누름으로 입력값이 action의 주소로 전달된다.
    - 버튼이 생기면 버튼이 엔터의 역할을 하게 되고 버튼의 내용을 작성할 수 있다.
  - form 
    - form을 통해서 사용자의 입력값을  받았을 때, 사용자를 대신해서 input으로 받은 입력값을  action="경로"로 지정해둔 경로로 이동해준다
    - input과 button을 form태그 안에 넣어줘야한다.
    - form +tab 을 하면 자동완성!

  ```html
  <form action="/result">
      <input name="id">
      <button>
          버튼내용
      </button>
   </form>
  ```

  

- 사용자가 입력한 값을 특정 검색엔진에서 검색하기

  - 검색엔진의 search 구조

    - ex) 구글의 서치 구조 : google.com/search?q=검색어

      - google.com/search
        : Google 검색 스크립트의 위치이다.

      - q=검색어
        : 파라미터(q와 사용자입력값인 검색어로 구성)
        : input된 사용자가 입력한 값을 어떤 이름("q")에 담아서(name="q") google.com/search? 뒤에 보내준다. 
        : 여기서 ? 는 파라미터가 검색 스크립트에 전달됨을 의미한다.
        : q는 실제로 구글이 쓰는 값이기 때문에 값을 바꾸면 제대로된 페이지가 나오지 않는다

  - 검색엔진모음페이지 구성(home.html) 

    ```html
    # 구글 검색 페이지에 연결 
        <form action="https://google.com/search">
            <input name="q">  # 구글의 파라미터는 q="검색값"의 형식
            <button> 검색 </button>
        </form>
    
    # 다음 검색 페이지에 연결
        <form action="https://search.naver.com/search.naver">
            <input name="query"> # 다음의 파라미터는 query="검색값"의 형식
            <button> 검색 </button>
        </form>
        
    # 네이버 검색 페이지에 연결   
        <form action="https://search.daum.net/search">
            <input name="q"> # 네이버의 파라미터는 q="검색값"의 형식
            <button> 검색 </button>
    ```

---



## 2. 전생에 나는?! 

- fake 패키지 
  - 참고 : https://github.com/joke2k/faker (제작자 페이지)
  - git bash 에서 pip install fake
  - vs code에서 from fake import Faker
  - 랜덤 이름, 랜덤 직업, 랜덤 주소 등을 제공하는 패키지
  - 여러 언어가 지원된다.

- 입력값을 받기

  ```python
  # app.py에서 라우팅작업
  # 홈페이지에서 링크가 걸려있다. (<a href="/pastlife">당신의 전생은?</a> 요로코롬)
  
  @app.route('/pastlife')
  def pastlife():
      return render_template('pastlife.html')
  ```

  ```html
  # pastlife.html
  <body>
      <h1>당신의 전생은?!</h1>
      <form action="/result">
          <p>당신의 이름은?</p>
          <input name="id">
      </form>
  </body>
  ```

  

- 결과값을 보여주기

  ```python
  #app.py에서 라우팅 작업
  
  @app.route('/result')
  def result(): 
      Job = fake.job()
      Name =request.args.get('id')
      #requests와 완전다르다. flask의 함수
      return render_template('result.html', Job=jobdict[Name], name=Name)
  ```

  ```html
  #result.html
  <body>
      <h1>{{name}}님의 전생은 {{job}} 였습니다. </h1>
  </body>
  ```

  

- 검색한 이름과 나온 랜덤 직업을 딕셔너리에 저장해 재 검색시 같은 결과 출력하기

  ```python
  # 딕셔너리를 전역변수로 설정해야 페이지에 들어갈 때마다 딕셔너리가 새롭게 리로드되는일이없다
  baitdict={}
  
  #app.py에서 라우팅 작업
  @app.route('/result')
  def result():
      Job = fake.job()
      Name =request.args.get('id')
      
      #만약 한번 나온 결과는 그대로 유지하려면? hint 딕셔너리 사용
      #우리 데이터에 해당하는 이름이 있는지 없는지 확인
      
      if Name not in baitdict.keys():
          baitdict[Name]=Job
          return render_template('result.html', job=Job, name=Name)
      else:
          Job = baitdict[Name]
          return render_template('result.html', job=Job, name=Name)
  
  #dictionary.keys()로 반환된 자료형은 dictionary keys 자료형. 리스트로 변환가능하다
  ```

---



## 3. 궁합을 알려드립니다. 

추억의 궁합을 알려드립니다. (참고 vonvon)

- 궁합을 보고 싶은 사람들의 이름을 입력값으로 받고

- randint(시작값, 끝값)으로 랜덤 값 출력해주기

  ```python
  # 홈페이지에서 링크가 걸려있다. (<a href="/goonghab">궁합보기</a>)
  @app.route('/goonghab')
  def goonghab():
      return render_template('goonghab.html')
  ```

  ```html
  # goonghab.html
  	<form action="/destiny">
          <p>당신의 이름</p>
          <input name="babo">
          <p>그 분의 이름</p>
          <input name="idol">
          <button>궁합보기</button>
      </form>
  ```

  ```python
  # app.py에서 라우팅작업
  @app.route('/destiny')
  def destiny():
      v=randint(51,100)
      babo= request.args.get('babo') #이름1
      idol= request.args.get('idol') #이름2
      return render_template('destiny.html', V=v, babo=babo, idol=idol)
  ```

  ```html
  # destiny.html 파일에서 결과 출력
  <body>
      <h1>{{babo}}님과 {{idol}}님의 궁합은 {{V}}% 입니다. {{babos}}</h1>
  </body>
  ```

  

- 미션 babo와 idol의 궁합값을 저장해두고 같은 입력값이 있을 때는 그 값을 가져오기

  - 내 답 : 사람이름들을 튜플로 받아 딕셔너리의 키에 집어넣기

  ```python
  v_dict={}
  @app.route('/destiny')
  def destiny():
      v=random.choice(range(51,101))
      babo= request.args.get('babo')
      idol= request.args.get('idol')
  
      if ((babo,idol) in v_dict.keys()):
          v= v_dict[(babo,idol)]
      elif ((idol,babo) in v_dict.keys()):
          v=v_dict.keys[(idol,babo)]
      else:
          v_dict[(babo,idol)]=v
      return render_template('destiny.html', V=v, babo=babo, idol=idol)
  ```

  - 선생님답 : 이중 딕셔너리 구조로 저장하기

  ```python
  babos={}
  # 처음부터 이중 딕셔너리를 선언할 필요도 없고(딕셔너리 안에 넣어줄 때 딕셔너리로 넣어주면 되기 때문에) 그리고 되지도 않는다.
  
  @app.route('/destiny')
  def destiny():
      v=random.choice(range(51,101))
      babo= request.args.get('babo')
      idol= request.args.get('idol')
  
  ## 이중딕셔너리 구조
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
  # babos[idol][babo]=v로 하면 에러가 뜨는데, 두번째 딕셔너리가 선언되지 않은 상태이기 때문이다.
  # babos[babo]={idol:v}로 하면 만약 두번째 딕셔너리가 없는 경우 새로 만들어지고, 있는 상태라면 키:값이 계속 추가된다.
      return render_template('destiny.html', V=v, babo=babo, idol=idol)
  
  ```

  

- showem.html을 만들어 바보들의 목록을 출력!

  ```python
  #app.py에서 라우팅
  #전역변수로 설정해줘야 리셋이 안된다.
  babos_list=[]
  @app.route('/admin')
  def showem():
      for k,v in babos.items():
          babos_list.append((k,v))
      return render_template('showem.html',babobabo=babos_list)
  ```

  ```html
  #showem.html에서 출력해주기
  <body>
      <p>바보들</p>
      <p>{{babobabo}}</p>
  </body>
  ```

---



## 4. 롤계정 승패확인



- 사용자의 계정을 입력하는 페이지

  ```python
  #app.py에서 라우팅
  @app.route('/opgg')
  def opgg():
      return render_template('opgg.html')
  ```

  ```html
   #opgg.html
  	<form action="/search">
          <p>아이디를 입력해주세요</p>
          <input name="userName">
          <button>전적검색</button>
      </form>
  ```

  

- 롤 승패정보페이지의 url은 https://www.op.gg/summoner/userName=유저계정 의 형태이다.

- 계정입력값을 이용해  해당 계정의 승패정보페이지에서 승패 값 스크래핑한다

  ```python
  #app.py에서 라우팅
  
  import requests
  from bs4 import BeautifulSoup
  
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
  #승패 값에 뒤에 w와 l가 붙어서 오기 때문에 떼어 주는 작업을 함
      return render_template('search.html',win=win,lose=lose,name=name)
  ```

  

- 그 결과를 출력하기

  ```html
  #search.html파일
  
  <body>
      <p>{{name}}님은 {{win}}번 이겼으며 {{lose}}번 졌습니다.</p>
  </body>
  ```

---



# 참고

- 성공한 서비스 예시
  : vonvon, bepro11
- git bash 명령어 
  : mkdir 파일명 (뒤에 확장자가 안붙으면 파일이 생성된다)

- 크롬에서 네이버가 나오게하기
  - https = 안전하다라는 뜻. secure . 왼쪽 클릭하면 보안연결 인증서를 사용함. 보안인증모듈을 사용하는데, 이때 이를 제대로 활용못해서 크롬에서 네이버를 켜지 못했다. 
  - 설정의 크립토 그래픽을 재설정했음 

