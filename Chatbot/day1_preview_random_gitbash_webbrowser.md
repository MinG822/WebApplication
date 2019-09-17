# Start Camp Chatbot (1st day)

*프로그래밍 언어는 1. 저장 2. 계산 3. 반복이 기본적인 구조*



*시작하기전에...*

- 스타트 캠프 챗봇프로젝트는 프로그래밍 맛보기 (1주일)
- 대/소문자, 띄어쓰기 및 들여쓰기( indent), 스펠링는 항상 주의하자
- slack 다운로드(커뮤니케이션 용), github & gitlab 계정생성(코딩 업로드 &포폴 용) 
- 챗봇주소 : http://s1.py.hphk.io

---

## 1. python preview

_모든 프로그래밍 언어는 다음 세 가지를 기본적으로 가지고 있음_

### 1. 저장

- 변수명 = 값
- ex) dust=60 : dust에 60이란 값을 저장한다. 
- cf) dust==60은 dust는 60과 같다는 의미.
- 저장할 수 있는 **값의 종류**는 크게 세가지
  1. 숫자 2. 글자(따옴표 필요) 3. 참/거짓(조건/반복에 사용)
- arryay of **list**
   : 박스의 리스트(리스트), 박스가 순서대로 여러개가 붙어있다. 대괄호사용, 인덱싱은 0부터 시작.
- **Dictionary**
  : 견출지를 붙인 박스 리스트, 중괄호로 묶어줌

### 2. 조건
-  if, elif, else

### 3. 반복 

- **while** 
  : 단순하게 순회하고자할 때 많이 쓰이게 된다. 
  : while대신 for사용 가능(더 편한 듯)

- **for**
  :for은 list등 반복가능한 자료형 앞에 in을 붙여 많이쓴다. 
  : ex) for i in list자료형: 정해진 범위 안에서 계속 반복되는 것

  :이때 i는 iteration의 줄임말로 아무거나 바꿔써도 되지만 가능한 명확하게 표시해 주는 편이 좋다.
  : for은 거의 모든 syntax에서 지원하기도 한다.

  

---



## 2. API와 Open Source

_오늘날 코딩은 거인의 어깨 위에서 하는 것. 전과 달리 매우 편하고 쉬워졌다. 모두 내가 만들 필요가 없음. 이를 가능케 하는 것이 API와 Open Source_

### 1. API (application programming interface)

- **다른 시스템 간의 커뮤니케이션 방식 (Interface)**
  : 응용프로그램에서 사용할 수 있도록 운영체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다. 
  : 리모콘 버튼 수= 인터페이스 수
  : 페북 로그인, 공공데이터 포털 등, 웹에서의 커뮤니케이션 방식은 요청(request)과 응답(response)으로 이루어짐

- **코드를 통한 접근성 (programming, programmable)**
  :  어떻게 작동하는지 몰라도 이용하는 형식을 알면 API를 활용 가능한다.
- 공공데이터 주소
   : https://www.data.go.kr/

### 2. open source

- 제작자의 권리를 지키면서 누구나 열람가능한 공개된 (소스)코드

- 만들어진 코드를 활용하기 == 오픈 소스 활용하기

- 다른 사람이 만든 코드를 잘 활용해보자!

  

---

## 3. python random함수를 활용한 lotto chatbot

- python 함수의 종류
  : 내장함수와 외장함수 두 가지

- 함수를 사용 방법
  : 내장함수는  그냥 사용 가능
  : 외장 함수는 install 후  import로 모듈을 불러와서 사용

-  **random** 모듈
  1. random.random(): 0 이상 1미만의 난수 반환
  2. random.randrange(시작, 끝): 시작 이상 끝 미만의 난수(정수) 반환
  3. random.shuffle(순서형자료): 자료의 원소 순서를 임의로 재배치
  4. random.choice(순서형자료): 자료에서 임의의 원소 하나 반환 
  5. random.sample(순서형자료, 반환원소 개수) : 비복원 표본 추출, 리스트로 반환

_tip : **a.b()** : a는 주어로, b는 동사로 인식하기(객체지향 프로그래밍)_

- 코드

```python
# 1. random 외장 함수 가져오기
import random
# 2. 1~45까지 숫자 numbers에 저장하기
numbers=list(range(1,46))
# 3. numbers에서 6개 뽑기
lotto=random.sample(numbers, 6)
# 4. 출력하기
print(sorted(lotto))
```



---

## 4. python 심화

다운로드: python 3.73, vs code, git

### 1. CLI(command line interface)의 종류

1. **유닉스 shell(sh, zsh, bash등)**
2. CP/M
3. DOS의 comand.com
4. etc...
5. 텍스트 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식을 뜻한다. 즉, 작업 명령은 사용자가 컴퓨터 키보드 등을 통해 문자열의 형태로 입력하며, 컴퓨터로부터의 출력 역시 문자열의 형태로 주어진다.

### 2. git bash 명령어 기초

- `ls` : list, 현재 디렉토리의 내용들을 나열
- `cd` : change directory 현재 있는 디렉토리를 이동함 
- `cd ..`: 상위 폴더로 이동하기
- tab을 누르면 자동완성
- `mkdir`: 새로운 디렉토리를 생성
- `pwd`: print working directory, 현재 있는 디렉토리의 위치를 알려줌
- `code`: visul code실행 명령문
- `code . `로 현재 있는 디렉토리에서 visul code실행
- `rm` : 파일 지우기
- `touch`: 파일 만들기
- `exit` : 터미널 종료

### 3. chocolatey?

1. 윈도우에서 패키지 설치 및 제거를 도와주는 프로그램
2. 관리자 권한으로 cmd실행
3. 설치 명령어 입력

### 4. vs code 기본 설정

- ctr+ shift + p : defualt shell 설정. 앞으로 python을 돌릴 때 gitbash를 통해 실행할 것이기 때문

- ctr+n: 새파일 만들기 항상 .py로 끝나야함

### 5. webbrowser 모듈을 이용해 웹브라우저를 켜보자

```python
import webbrowser
url="http://search.daum.net/search?q="
keyword=["네이버", "다음", "구글"]
for key in keyword:
    webbrowser.open(url+key)
```

