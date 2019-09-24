# Django

 *이 문서는 Django의 활용법을 정리하기 위해  [공식홈페이지](https://www.djangoproject.com/)를 참고하여 개인적으로 작성한 글입니다.*

---

## 0. Django란?

- Django는 파이썬 언어를 활용한 웹 프레임워크
- Django를 이용하면 매우 간단하게 웹 서비스를 만들수 있기 때문에, Django 이용자들은 구현하고자하는 앱 서비스에만 오롯이 집중 할 수 있다.
- 무엇보다 Django는 오픈 소스이기 때문에 누구나 무료로 사용할 수 있다. 

---

## 1. Django 시작하기

- Django 의 버전은 2.1, 2.2 까지 나왔으며, 파이썬 3.5, 3.6, 3.7 버전을 통해 이용할 수 있다. 

- Django 공식 배포를 이용하기 위해서는 pip 로 install 해주면 된다.

  ```bash
  $ pip install Django
  ```

- MySQL이나 Oracle과 같은 대용량의 데이터베이스 엔진을 이용하고자 할 경우, 또는 기존에 사용하고 있던 데이터베이스가 있다면 개별적으로 데이터 베이스도 설정을 해주어야한다.  그렇지 않을 경우 필요없다면 Django 에서 SQLite를 간단하게 이용할 수 있어 별도의 데이터베이스를 설정해줄 필요가 없다.

---

## 2. Django 프로젝트 생성

- project란?

  : 장고 인스턴스에 대한 모든 설정을 담은 파이썬 패키지로 데이터베이스 설정, 장고 설정 및 애플리케이션 설정등을 포함한다.

- 프로젝트 생성 명령어 : `$ django-admin startproject MYSITE`

- 프로젝트 디렉토리의 파일 구조

  ```
  MYSITE/
  	manage.py
  	mysite/
  		__init__.py
  		settings.py
  		urls.py
  		wsgi.py
  ```

  - manage.py는 django-admin처럼 동작하는 커맨드라인 유틸리티다.
  - urls.py는 장고 프로젝트에서 사용하게 될 url들을 선언하고 해당 url로 요청이 들어올시 어떻게 처리할 것인지 설정할 수 있다.

- django 프로젝트 개발 서버 시작하기

  - `$ python manage.py runserver`를 통해 만들어진 프로젝트의 개발서버를 시작할 수 있고 http://127.0.0.1:8000/을 통해 접속해 확인할 수 있다. 

---

## 3.Django 앱 생성

- app vs project

  앱 : 특정한 기능(블로그 등)을 수행하는 웹 어플리케이션. 다수의 프로젝트에 포함될 수 있음

  프로젝트 : 특정 웹사이트를 위한 앱들과 각 설정들을 한데 묶어둔 환경. 다수의 앱 포함 가능

- 앱 생성 명령어 : `$ python manage.py startapp blog`

  blog라는 이름의 앱을 생성했으며, 어떤 곳에든 생성할 수 있지만 편의상 MYSITE 의 하위폴더로 생성했다.

- 프로젝트와 앱의 디렉토리 구조

  ```
  MYSITE/
  	blog/
  		__init__.py
  		admin.py
  		apps.py
  		migrations/
  			__inig__.py
  		models.py
  		tests.py
  		views.py
  	mysite/
  		__init__.py
  		settings.py
  		urls.py
  		wsgi.py
  	manage.py
  ```

- 앱의 MTV 구조(소프트웨어의 패턴)

  - models(M) 

    앱의 데이터를 일정한 형식으로 저장하는 역할. 부가적인 메타데이터를 가진 데이터 베이스의 레이아웃을 말함

  - Template(T)

    앱의 데이터를 표현하는 형식(보통 HTML파일을 사용했음)

  - View(V)

    페이지 렌더링을 담당하는 함수(url을 요청했을 때 담당 함수를 통해 기능하고 template으로 연결)

- 생성한 앱을 프로젝트에서 사용하기 위해서는 `MYSITE/mysite/settings.py` 의 `INSTALLED_APPS`에 blog 앱을 추가해 주어야한다. `INSTALLED_APPS`는 장고 인스턴스에서 활성화된 모든 장고 어플리케이션들의 이름이 들어가 있는데, 상위에 앱이 있을 수록 작업 수행 시 우선순위가 높다.

  ```python
  INSTALLED_APPS = [
      'blog',
      'django.contrib.admin', # 관리용 사이트
      'django.contrib.auth', # 인증 시스템
      'django.contrib.contenttypes', # 컨텐츠 타입을 위한 프레임워크
      'django.contrib.sessions', # 세션 프레임워크
      'django.contrib.messages', # 메세징 프레임워크
      'django.contrib.staticfiles', # 정적 파일을 관리하는 프레임워크
  ]
  ```

---

## 4. 모델

- 다시 정리하면 장고에서 모델이란 
  : 앱의 데이터를 일정한 형식으로 저장하는 역할을 하며 부가적인 메타데이터를 가진 데이터 베이스의 레이아웃

- 생성할 앱이 데이터베이스를 활용해야한다면 MTV 중 models 부터 접근하는 편이 좋다고 배웠다. 
  - 앱을 만들어가면서 데이터베이스를 업데이트하기 보다 사용할 데이터들의 관계를 파악해 앱의 `models.py`에 데이터베이스를 설계해 생성하는 편이 덜 번거로우며 
  - 앱을 역시 보다 논리적으로 만들 수 있기 때문이다. 
  - [Don't Repeat Yourself 원칙](http://wiki.c2.com/?DontRepeatYourself)
    중복성을 최대한 피하고 정규화하여 고유한 개념 및 데이터를 단 한 번, 단 한 곳에 존재하는 것이 좋는 원칙
- SQLite는 파이썬에서 기본으로 제공되기 때문에 별도로 설치할 필요가 없지만 실제 프로젝트에서는 PostgreSQL과 같이 확장성있는 데이터베이스를 사용하길 권한다고 한다. SQLite이외의 데이터베이스를 설치하고 django에서 설정하는 방법은  [여기](https://docs.djangoproject.com/ko/2.2/intro/tutorial02/)를 참고하기.
- 모델을 변경하고 데이터베이스를 생성하는 단계는 다음과 같이 크게 세 단계이다.
  1. `models.py`에서 모델 변경하기
  2. `python manage.py makemigrations`를 통해 변경사항에 대한 migration을 만들기
  3. `python manage.py migrate` 명령을 통해 변경사항을 데이터베이스에 저장하기
- migration을 만드는 명령과 적용하는 명령이 분리된 것은 버전관리 시스템에서 마이그레이션을 커밋하고 앱과함께 출시 할 수 있도록 하기 위해서

---

### 4.1. models.py  에서 모델 변경하기

- `models.py`에서 데이터베이스에 저장하고 싶은 테이블을 클래스로 작성하는 방식으로 모델을 변경할 수 있다.

- 예를 들어 제목, 내용, 이미지파일, 저장된 시각, 수정된 시각에 대한 데이터들로 이루어진 블로그의 포스트를 저장할 데이터베이스를 만들고 싶다면 `models.py`에 Post라는 클래스를 생성하고, 테이블에 저장될 데이터들을 필드를 지정해야한다.

  ```python
  from django.db import models
  class Post(models.Model): 
    title = models.CharField(max_length=25)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  ```

  - 데이터베이스 테이블 Post
  - django.db.models.Model이라는 클래스를 상속받는 서브클래스로 표현
  - Post의 필드
    - Post 모델의 변수로 models의 Field클래스의 인스턴스로 표현
    - 이때 데이터베이스의 각 필드는 어떤 자료형을 가질 수 있는 지 django에게 알려줌.
    - 자료 변수명은 데이터베이스에서 칼럼명으로 사용됨.
    -  Field 인스턴스의 이름을 설정하고 싶다면 
      `content = models.TextField('content of post')`와 같이 첫번째 위치 인자로 Field 인스턴스의 이름 전달
    - ImageField의 인자로 `blank=True`을 전달하기 때문에, 빈 값이 허용될 수 있음.

  

- **Field클래스의 종류**

  - **CharField(max_length)**

    - 비교적 작은 사이즈의 문자열 자료형을 가지는 필드
    - 필수 인자로 max_length를 가짐

  - **TextField()**

    - 큰 사이즈의 문자열 자료형을 가지는 필드

  - **DateTimeField(), DateField(), TimeField()**

    - 각각 datetime.datetime, datetime.date, datetiem.time 인스턴스를 자료형으로 가지는 필드

    - 선택 속성(attribute)

      **DateField.auto_now** : model클래스의 객체가 저장될 때마다 자동적으로 현재시각이 모델에 저장되는 옵션이며 마지막으로 수정된 타임스탬프를 표현하는데 유용하다.

      **DateField.auto_now_add** : model클래스의 객체가 처음 생성될 때 자동적으로 저장되는 옵션이다.

    - 만약 이상하게 DateField 데이터가 이상하게 저장된다면 프로젝트의 `settings.py`의 `TIME_ZONE = 'Asia/Seoul'`로 되어있는지 확인

  - **FileField()와 ImageField()**

    - 업로드된 파일의 상대경로가 저장되는 필드

    - 선택 속성(attribute)

      - 업로드된 파일이 저장되는 세부 경로를 지정해줌

      - 지정해주지 않을 때 `FileField.upload_to=None`가 디폴트로 넘겨지며, 업로드된 파일은 MEDIA_ROOT 에 파일이 저장됨

      - 지정해 줄때는 `FileField.upload_to='uploads/'`와 같이  `MEDIA_ROOT/`의 하위 디렉토리를 값으로 넣어줄 수 있으며, 업로드된 파일은 `MEDIA_ROOT/uploads`에 저장된다.

      - 효율적인 파일관리를 위해 `FileField.upload_to='uploads/%Y/%m/%d/'`로 설정해 날짜에 따라 파일을 분류해 저장할 수도 있다.

      - **MEDIA_ROOT와 MEDIA_URL설정**

        - MEDIA_ROOT

          - 사용자가 업로드한 파일들을 저장할 로컬 디렉토리에 대한 절대파일경로

          - 장고의 성능을 위해 데이터베이스에 직접 파일을 저장하지 않고, MEDIA_ROOT에 지정된 경로로 저장된다

          - MEDIA_ROOT 예시

            MYSITE프로젝트 폴더 내의 media 폴더에 사용자가 업로드한 파일들을 저장하고 싶을 경우

            `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`

          - STATIC_ROOT와 다르며, STATIC_ROOT가 설정되기 전까지는 MEDIA_ROOT가 그 역할을 대신 수행해주지만 보안에 취약.

        -  MEDIA_URL

          - 데이터베이스 테이블의 image 컬럼에 실제로 저장되는 값(URL)으로

          - MEDIA_URL을 통해 MEDIA_ROOT로 부터 미디어 파일을 불러오거나 관리

          - 디폴트는 빈문자열이며 디렉토리를 지정할 경우 반드시 /로 끝나야한다.

          - STATIC_URL과는 다른 값이다

          - 인터넷 상의 이미지 주소를 가져올 수도 있고, 로컬폴더의 경로를 지정해줄 수도 있다.

          - 로컬폴더의 경로 지정 예시

            - 위에서 설정한 MEDIA_ROOT의 이미지 파일의 경로를 가져오고 싶을 경우

              `MEDIA_URL = '/media/'`

            - 로컬로 저장한 이미지 파일의 경로를 사용자가 요청했을 때 불러오기 위해서는 `MYSITE/mysite/`을 다음과 같이 작성해야한다.

              ```python
              from django.contrib import admin
              from django.urls import path, include
              from django.conf.urls.static import static
              from django.conf import settings
              urlpatterns = [
                path('admin/', admin.site.urls),
              ]
              urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
              ```

  - 그 외의 Field 클래스의 종류(자세한 내용은 [여기](https://docs.djangoproject.com/ko/2.2/ref/models/fields/#django.db.models.CharField)를 확인하기)
    - 정수 자료형을 저장하는 IntergerField() 
    - (직접 쓸 일은 없지만 primary key를 자동으로 설정 및 저장하는 필드도 IntergerField로 설정되어 있음)
    - checkboxinput 등을 사용할 경우 ture/false값을 저장하는 BooleanField()
    - timedelta값 등 기간 값을 저장하는 DurationField
    - 유효한 이메일 주소인지 확인해주는 EmailField()
      

- 1:N 다대일 관계의 데이터베이스

  ```Python
  from django.db import models
  class Post(models.Model): 
    title = models.CharField(max_length=25)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
  class Comment(models.Model):
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
  ```

  - Post 클래스의 인스턴스를 Comment 클래스(모델)의 외래키(Foreign Key)로 지정해서 다수의 Comment 클래스 인스턴스들이 하나의 Post 클래스의 인스턴스를 가리키는 관계데이터베이스를 표현

---

### 4.2. 모델 활성화하기

- `models.py`을 활성화하면 django가 앱의 데이터베이스 스키마를 생성하고 (CREATE TABLE) 모델 객체에 접근하기 위한 데이터베이스접근 API(`python shell`에서 조작가능)를 생성한다.

- **makemigrations**

  -  `$ python manage.py makemigrations`
  -  모델을 변경시킨 사실과 이 변경사항을 migration으로 저장시키고 싶다는 것을 django에게 알려줌
  -  **migration**이란 장고가 데이터베이스 스키마를 포함한 모델의 변경사항을 저장하는 방법으로써, `0001_initial.py`과 같은 파일들로 저장됨. 수동으로 직접 변경도 가능하다고 함.
  -  migration이 내부적으로 실행하는 sql 문장들을 확인하고 싶으면 `sqlmigrate` 명령어를 통해 확인할 수 있다.

- **migrate**

  -  `$ python manage.py migrate`
  -  데이터베이스에 모델과 관련된 테이블을 생성하거나 테이블을 업그레이드 해준다.
  -  아직 적용되지 않은 마이그레이션을 모두 수집해 이를 실행하며 이를 통해 모델에서의 변경사항들과 데이터베이스의 스키마의 동기화가 이루어지기 때문에, 동작 중인 데이터베이스를 자료 손실 없이 업그레이드 하는데 최적화 되어있음
  -  명령어를 실행했을 때 장고가 탐색하는 곳은 mysite/settings.py의 Installed_apps과 각각의 app과 함께 제공되는 데이터베이스 migrations이기 때문에 모델 활성화 하기 전에 반드시 Installed_apps에 앱을 등록해야한다. 

- Python shell (Django API) 로 데이터베이스 객체 생성 및 조작하기

  -  `$ python manage.py shell`는 django에서 동작하는 모든 명령을 대화식 phython shell에서 그대로 실행할 수 있음

  ```shell
  >>> from blog.models import Post 
  # models.py의 Post 클래스 객체를 가져온다
  >>> Post.objects.all()
  <QuerySet []>
  # Post클래스의 모든 인스턴스들을 가져오는 명령어. 현재 생성된 인스턴스가 없기 때문에 쿼리셋은 비어있다.
  >>>article = Post(title="title", content="content")
  # Post클래스의 인스턴스로 article을 생성하는데, created_at과 updated_at은 자동으로 생성되고, image는 빈 값도 허용되기 때문에 title과 content만 지정해도 생성된다.
  >>>article.save()
  # 명시적으로 저장을 해줘야 데이터베이스의 Post 테이블에 article 튜플이 저장된다. 
  >>>article.id
  1
  # article의 id
  >>>article.title
  title
  >>>article.title = "newtitle"
  >>>article.save()
  >>>Post.objects.all()
  <querySet [<Question: Question object (1)>]
  >>>Post.objects.filter(id=1)
  <querySet [<Question: Question object (1)>]
  >>>Post.objects.get(pk=1)
  <querySet [<Question: Question object (1)>]
  >>>Post.objects.first()
  <querySet [<Question: Question object (1)>]
  >>>Post.objects.last()
  <querySet [<Question: Question object (1)>]
  >>>article.delete()
  ```

---

## 5. 뷰 작성하기

MTV 에서 V를 담당

1. 