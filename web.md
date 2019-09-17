# Intro to WEB Service

### Web Service

- web

  - 월드 와이드 웹(World Wide Web, WWW, W3)
  - 인터넷에 연결된/ 컴퓨터들을 통해/ 사람들이 정보를 공유할 수 있는 전세계적인 정보 공간

- service

  - 고객(client)의 요청(request)과 서버(server)의 응답(response)

- web service

  - server computer

    서버용 컴퓨터에서 서버 역할을 하는 것은 소프트웨어

    클라우드 서버는 필요한 만큼만 서버를 빌리는 것

  - server가 클라이언트(client)들에게

  - 브라우저(Browser)

  - 요청의 종류

    - 줘라(Get) (read)
    - 받아라(Post) (create)
    - 요청이 잘 되었는지는 status로 확인 할 수 있다.
    - update, delete에 해당하는 요청들에 대해서도 배우게 된다.

  - user에 의한 request, program에 의한 response

  - 서버용 컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다.

- Static Web

  - 클라이언트가 요청을 보내면 서버가 응답한다.

  - 요청이 다양하게 들어올 것을 예측하는 것이 아니라 어떤 요처이 들어와도 같은 형식으로 제공한다.

  - 블로그나 소개 페이지들

  - 클라이언트가 요청을 보내는 프로그램? 

    - Chrome the browser

      웹의 표준이며 요새는 작은 os와 같이 동작한다.

      웹사이트는 결국 남의 컴퓨터 주소/dir1/dir2/.../WantThis.file을 불러오는 것이다.

      이때 172.217.27.78는 ip, 컴퓨터의 고유번호 값이다.

      사람에게 친숙한 도메인으로 google.com (컴퓨터 주소) ip주소를 변환

      ip주소와 domain을 변환(mapping)해주는 역할을 하는 서버 프로그램은 dns

      proxy는 중간에 서버를 만들어 사용자가 요청할 때 그 서버를 거쳐가게 만드는데 이때 개인정보를 뽑아간다.

- Dynamic Web 또는 Web Application program(Web APP)

  - 주문서의 패턴에 맞춰서 보내줄 수 있는 웹

  - URI 통합 자원 식별자

  - URL (Uniform Resource Locator, 파일식별자)

    네트워크 상에서 자원이 어디있는지를 알려주기 위한 고유 규약

    웹사이트 주소 뿐만 아니라 컴퓨터 네트워크상의 자원을 모두 나타낼 수 있다.

### 실습

깃 허브를 통한 static webservice 배포: MinG822.github.io