# Start Camp (Day2)

- webbrowser 모듈에 대한 설명
  :oepn, open_new, open_new_task

_웹 브라우저저에 이어 좀 더 복잡한 Task를 맡겨보자_ 

## 1. 정보 스크랩하기
_일상에서 코스피 지수나 부동산 가격 등 자주 확인하는 정보를 자동으로 스크랩해보자._

### 1. 배경 ###

- 보통은 1. Naver에 들어간다. 2. 정보를 검색한다. 3. 원하는 정보만 복사한다. 4.내 컴퓨터에 저장한다.의 단계로 이루어지는데, 

- 이때 정보를 검색(request)하고 받는 것(response)은 웹서비스의 기본적인 패턴
  : service는 client의 request, sever의 response를 공통적인 패턴으로 가지고 있음
  : webservice(onlineservice)는 (offline과 다르게) 모두 url을 통해 요청하고 응답한다.
  : 그래서 사실상 해당 url주소의 문서(페이지 소스)를 주고받는 것
  : 내가 어떤 정보를 스크랩하려면 페이지 소스에서 가져와야하는 것
  
  

### 2. request 모듈 이용하기 ### 

1. **requests 패키지 다운로드(GitBash)**
   1. pip list : 파이썬의 패키지 리스트 확인
   2. 없다면: pip install 패키지명
   3. 이때 상호작용하는 다른 패키지들도 함께 다운로드됨
   4. code . 로 visual code로 넘어오기

2. **requests**
   1. **requests.get(주소)**
      : request를 저장한 변수를 print하면 response가  뜬다. 
      : 이때 200은 잘된 것
      : 크롬의 개발자 모드에서 Network를 확인했을 때  성공적이면 request method는 get, 그리고 status 는 200대 라인의 숫자가 나온다.
      
   2. **requests.get(주소).txt**
      : 주소를 쳤을 때 그 주소의 페이지 내용을 얻고 싶을 때
      
   3. **requests.get(주소).status_code**
      : 위에서 설명한 status를 확인하고 싶을 때
      
      

### 3. **bs4의 BeautifulSoup**

- 파싱해 주는 패키지
- **파싱**
  :우리 눈에는 똑같지만 파이썬에게는 식별자 id를 기준으로 광속검색이 가능하도록 예쁘게 전달해주는 것
- install bs4
- bs4.BeautifulSoup(받아온 페이지)
- 패키지 이후에 : 
  1. 웹브라우저에서 원하는 정보의 아이디 값을  우클릭 검사 -> 복사 -> css선택자 : #KOSPI_now 
  2. select_one(원하는 정보)
  3.  _원하는 정보는 html 로 작성된 코드에서만 가져올 수 있다. 페이지가 자바로 쓰여진 코드로 이루어지면 동적언어라 요청한 시점에 정보가 없어서 가져 올 수 없다._
3. .text를 붙이면 코드가 아닌 정보 그 자체만 나옴
4. 실습코드

```python
import requests
import bs4

url="https://finance.naver.com/sise/"
response = requests.get(url).text
document = bs4.BeautifulSoup(response,'html.parser')

'''
두번째 인자로 'html.parser'로 넣어준 이유는 경고 때문 : kospi.py:5: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
'''

kospi = document.select_one('#KOSPI_now').text
print(" 현재 코스피 지수는 : "+ kospi)
```

5. 미션

```python

# Mission 검색어의 1위부터 10위까지 가져오는 코드를 작성해보자

# 내 답

import requests
import bs4

url2 = "https://www.naver.com/"
response2 = requests.get(url2).text
# print(response2)
document2 = bs4.BeautifulSoup(response2, "html.parser")
# print(document2)
rank1keyword = document2.select('html body div#PM_ID_ct.wrap div.header div.section_navbar div.area_hotkeyword.PM_CL_realtimeKeyword_base div.ah_list.PM_CL_realtimeKeyword_list_base div.ah_tab a.ah_tab_btn')
# 이때 css path를 선택했다. 

for i in range(0,10):
    print(rank1keyword[i].text)
import requests
import bs4

# 선생님 답


url3 = "https://www.naver.com/"
response3 = requests.get(url3).text
# print(response3)
document3 = bs4.BeautifulSoup(response3, "html.parser")
# print(document3)
rank1keyword = document2.select('.ah_a')
## 웹에서 가져올 때 css selector를 선택했다.

for i in rank1keyword:
    print(i.text)
    
# selector을 선택하는 것과 path를 선택하는 것의 차이는?
```

---

## 2. python 버전 정보 업그레이드

nstall 패키지 를 하려면 python 의 버전 정보를 업그레이드 해야함_

- **python의 버전 정보 업그레이드**
  - GibBash>  python --version 으로 버전확인
  - 내컴퓨터의 속성에 시스템 속성에 고급에 환경변수에 Path의 제거할 부분을 없애기
    1. C:\Program Files\Python35\Scripts\ 
    2. C:\Program Files\Python35\
  - 명령할 때 경로를 굳이 일일이 써주지 않아도 되도록 컴퓨터의 환경 변수에 경로를 저장해 뒀던 건데 이제 python 구버전의 경로가 필요없어진 것이니 이 변수를 제거한 것.
  - 다시 3.5버전을 쓰고 싶다면 위의 환경변수들을 다시 추가하면 된다. 
  - 변경사항 적용하려면 리부팅 필요
  - 지우고 나서 python 버전확인시 업그레이드가 되어있는 이유는 새 버전을 다운받은 위치에 저장된 path경로가 검색되기 때문에. (컴퓨터가 환경변수를 가져오는 우선순위는 내 컴퓨터 > 유저)

---

## 3. git 과 github 

_개발자에게 git과 github는 필수! 그렇지만 처음에 익숙해지는 것은 어렵다_

- **git**
  - 코드 관리 시스템
  - 분산화된 작업환경에서 코드 관리를 효율적으로 하기 위해서 발명됨
  - git은 내 로컬 컴퓨터 안에 있는 내 코드를 관리하는데 도움됨
  - 깃을 추가하고 저장하는 건 오프라인 로컬 영역에서 이루어진다.
  - 폴더마다 깃을 저장할 수 있는데, 뭔가 변화되면 항상 git hub에 올려야한다!
  - 새로운 리포지토리에 이미 올린 폴더를 올리고 싶으면 만들어진 깃을 삭제하고 새로운 깃을 만들어야하는데, 한번 리포지토리에 설정된 깃은 업로드시 경로 역할을 하기 때문 
- **github**
  - 깃이 관리한 내 코드들을 온라인에서 공유하기 위해서 
  - 항상 최종본으로 업데이트 해두는 것이 좋다
  - push라는 명령어가 원격으로 업로드하는데 이부분이 온라인 상에서 작업 
  - push origin master로 하는 것이 좋다. 그래야 내 계정에서 올린 코드가 되기 때문
  - 다운로드 받을 때는 git clone을 이용하는데 이는 리포지토리를 복제하는 것
  - git clone (clone with HTTPS)



- **git으로 github에 코드를 업로드 하는 방법**

  1. **git add** 파일 이름 또는 . (저장할 파일 목록에 파일 추가)
  2.  **git commit -m** "메시지내용" (저장단계)/(여기까지는 우리 컴퓨터에서 일어나는 단계)
  3.  **git push origin master** (온라인으로 업데이트)
     - commit 은 save라는 뜻 
     - 만약 git commit 을 쓰게 되면 **esc-> :(콜론) -> wq으로 탈출하기 !**
     - **git status(현재 상태), git log(지금까지의 저장내역)**
     - 로그인을 한번 해두면 인증을 두번 할 필요가 없다.

  - 언제 어디에 있든 깃 허브에 저장 가능 또 저장한걸 새로운 환경에서도 다운받을 수 있다.
    (집에서도 직장에서도 )
    - 다운받을 때는 git pull origin master로!

  

---



## 4. python에서 컴퓨터 조작 with 모듈 os 

- git bash 명령어와 파이썬 os 명령어의 비교

  | git bash 명령어              |                                     | 파이썬 os모듈 명령어 |
  | ---------------------------- | ----------------------------------- | -------------------- |
  | ls                           | 해당 위치의 파일목록탐색            | os.listdir()         |
  | mv 해당 파일 명 바꿀 파일 명 | 파일 이름 바꾸기                    | os.rename            |
  | touch                        | 파일만들기                          |                      |
  | rm                           | 파일지우기                          |                      |
  | cd 파일                      | 해당 파일 위치로 이동               | os.chdir('파일명')   |
  |                              | git bash에서 쓰던 명령어를 쓰게해줌 | os.system()          |

  

- 실습

  ```python
  os.system(f"touch report{0}.txt") 
  # str.format과 같은 것. f string이라고 부른다. 3.6부터 지원
  os.system("touch report{0}.txt".format(i)) 
  os.rename("report{0}.txt".format(i), "SSAFY{0}.txt".format(i))
  
  #또는
  file = os.listdir()
  for i in file:
      os.rename(i, i.replace("SSAFY","ssafy"))
  ```

  

---

## 5. python 내장함수로 파일 읽고 쓰기

_파이썬 내장함수로도 파일을 생성하고 내용을 작성하거나 읽어올 수 있다!_

-  순서 

  1. open('(경로)새파일명', '파일열기모드')
     : 파일열기 모드에는 세가지 종류가 있다.

     | 파일열기모드 | 설명                                                         |
     | ------------ | ------------------------------------------------------------ |
     | r            | 읽기 모드                                                    |
     | w            | 쓰기 모드                                                    |
     | a            | 추가 모드<br />읽기와 쓰기모드와 달리 내용을 덮지 않고 추가할 수 있다 |

  2. read 나 write함수로 파일을 읽거나 쓰기

     - write모드의 함수
       : 파일변수.write(파일에 적을 내용)
       : 쓰기모드로 파일을 열때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라짐

     - read모드의 함수

     | read모드의 함수      | 설명                                                         |
     | -------------------- | ------------------------------------------------------------ |
     | 파일변수.read()      | 파일 내용 전체를 문자열로 돌려준다.                          |
     | 파일변수.readline()  | 파일의 가장 첫번째 줄을 읽어준다.                            |
     | 파일변수.readlines() | 파일의 모든 줄을 읽어서 각 줄을 요소로 갖는 리스트를 돌려준다. |

     - add모드
       : 원래 파일의 내용을 유지하면서 새로운 내용을 추가하고 싶을 때
       : add모드로 열고 파일변수.write(파일에 추가할 내용)

  3. 현재 파일이 열려있기 때문에 파일변수.close()로 파일 닫아주기

- 실습

  ```python
  f= open('ssafy.txt','w')
  print(dir(f)) 
  # dir은 해당 객체로 뭘 할 수 있는지 나온다.
  f.write('hello ssafy')
  #쓰기모드
  f.close()
  # 항상 꼭 닫아줘야한다.
  ```

- with 문으로 open과 close를 자동화 시키기

  ```python
  with open('ssafy.txt','w',encoding='utf-8') as f:
      f.write('위드를 썼다\n'*5)
  #이러면 클로즈를 안해도된다
  
  with open ('ssafy.txt','r',encoding='utf-8') as f:
      #  result=f.read()
      #  print(result)
       result2=f.readlines()
       print(result2)
  ```

  

- 미션

  ```python
  # 1. problem.txt 파일 생성 후, 다음과 같은 내용을 작성
  0
  1
  2
  3
  # 2. problem.txt의 파일 내용을 다음과 같이 변경
  3
  2
  1
  0
  
  # 간단한 해결
  
  with open("problem.txt",'w') as f:
      for i in range(4):
          f.write("{}\n".format(i))
  with open("problem.txt",'w') as f:
      for i in range(3,-1,-1):
          f.write("{}\n".format(i))
          
  #writelines() 와 reversed()를 이용한 해결
  
  with open("problem.txt",'r') as f:
       result=f.readlines()
       result2=reversed(result)
  
       
  with open("reversed.txt",'w') as d:
      d.writelines(result2)
       
  ```



---



## 참고

- coursera, mooc, edx(cs50), udacity

- udacity 는 git과 머신러닝을 잘가르친다_ 



- Visual Studio Code 에서 코드를 실행할 때

  - ctr + F5
  - 또는 터미널에서 python 파일명.py 을 명령한다.
  - tip: block + ctr + / -> 커맨트 아웃(주석처리)

  



