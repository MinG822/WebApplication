# CSS

HTML 은 정보와 구조화(Content) CSS는 styling의 정의(Presentation)

각자 문법이 다른 별개의 언어이다. 만들어진 시점, 체계, 사고구조, 주체 모두 다르다.

## 1. 기본 사용법

```css
h1{color:blue; font-size:15px;}
```

셀렉터 {선언; 선언; 선언} 으로 이루어져있다. 여기서는 h1이 셀렉터(selector), color: blue가 선언인데, color은 프로퍼티(property, 속성), blue는 값(value)이다.

css 활용하기

1. Inline(인라인)

   HTML 요소의 style에 CSS를 넣기

   html 태그 안에 style을 일일이 쓴다면 가독성이 안좋아지고 재활용이 힘들어진다.

   ```html
   <h1 style="color:blue; font-size:100px">
       This is my site
   </h1>
   ```

2. Embedding(내부참조)

   HTML 내부에 CSS를 포함시키기

   인라인보다는 가독성이 좋고 재활용할 수 있다.

   ```html
   <head>
       <style>
           h1 {
               color: blue;
               fontsize: 100px;
           }
       </style>
   </head>
   ```

3. link file(외부참조)

   외부에 있는 CSS 파일을 로드하기. 표준적인 방법이다.

   네이버같은 경우는 css만해도 스타일 시트가 몇천줄이다. 웹에서 확인할 때 css beautifier, 사람에겐 beautifier, 기계에겐 uglifier. uglifier는 공백 없이 바꿔줌. 용량을 줄이기 위한 목적. 

   보통 css파일은 style.css라고 파일명을 짓는다. 

   ```html
   <head>
       <link rel="stylesheet" href="mystyle.css">
   </head>
   ```

   ```css
   h1 {
       color:blue;
       font-size:20px
   }
   ```

   - link 태그는 외부의 문서를 연결시키는 태그. link태그를 이용해 css파일같은 스타일 시트 파일을 연결할 수 있다. 파이썬의 import와 비슷하다고 생각하면 된다..
   - link 태그는 head 부에 위치한다.
   - href에는 연결할 곳의 주소를 쓰는데 절대 주소, 상대주소 모두 가능하다. 
   - rel 은 현재 문서와 연결문서의 관계를 표시하는데 (외부블로그참고)
     - stylesheet는 스타일시트로 연결할 때
     - alternate문서의 대안버전(프린트나 번역사이트)로 연결할 때

- author 저작자로 연결할 때
  - help 도움말로 연결할 때
  - license 문서의 저작권 정보로 연결할 때
  - search 검색도구로 연결할때 등등이 있다. 
- 다른 속성으로 type도 있는데, type은 연결 문서의 MIME 유형(href 속성이 설정될 때만 사용함)을 가리키며 MIME이란 multipurpose Internet Mail Extensions로 원래 전자 메일 전송을 위한 인터넷 표준이었으나 현재는 웹에서 내용 유형(content type)을 말할 때 자주 쓰인다. MIME type은 대표적으로 css 파일의 경우 text/css, js 파일의 경우 text/javascript, xml 파일의 경우 application/xml이다. 
- 실제 프로젝트에서 활용한다면 어떤 것을 사용해야할까?
  - 컴포넌트화. 일반적으로 외부 파일로서 활용한다.
  - 성격이 다른 코드들을 파일 단위로 분류함, html, css, static, dynamic 등 구분해서 

------

## 2. CSS 단위

프로퍼티 값의 단위

1. 키워드

   개발자 도구로 확인해 볼 수 있는데

   예를들어 display의 값으로는 block, contents, flex, grid, inline, none, table 등등이 있다.

2. 크기 단위

   우리가 알고 있는 크기 단위

   - px : 이때 픽셀(pixel)은 화면을 구성하는 단위로 픽셀수가 많은 고해상도일 수록 이미지를 더 선명하게 표현할 수 있다. 디바이스별로 픽셀의 크기는 제각각이다. 대부분의 브라우저는 1px을 1/96 인치의 절대단위로 인식한다.
   - % : 백분율 단위의 상대 단위이다. 요소에 지정된 사이즈(상속된 사이즈나 디폴트 사이즈)에 상대적인 사이즈를 설정한다.
   - em: 배수 단위로 상대단위이다. 백분위의 업글판이라고 생각하면 된다. 요소에 지정된 사이즈(상속된 사이즈나 디폴트 사이즈)에 상대적인 사이즈를 설정한다. 문제점으로 상대적인 값이기 때문에 상속이나 예상치 못한 값들이 나타날 수 있다. CSS는 상속을 받는 언어 중에 하나고 복잡한 상속구조를 가지고 있다. 즉 상황에 따라 1.2em은 각기 다른 값을 가질 수 있다. 일일이 신경써야해서 귀찮다.
   - rem: root em으로 rem은 최상위 요소(html)의 사이즈를 기준으로 삼는다. 예를들어 font-size:1rem 은 html 요소의 font size와 같으며 이때 대부분의 브라우저에서 디폴트 값은 16px이므로 1rem역시 16px이다. rem 의 단점으로는 가늠하기 어렵다는 점이 있다.
   - Viewport : 디바이스마다 다른 크기의 화면을 가지고 있기 때문에 상대적인 단위인 viewport를 기준으로 만든 단위이다. vw는 너비의 1/100, vh는 높이의 1/100, vmin은 너비 또는 높이 중 작은 쪽의 1/100, vmax는 너비 또는 높이 중 큰 쪽의 1/100이다. IE 8 이하는 지원하지 않으며 IE 9~ 11, Edge는 지원이 완전하지 않으므로 주의가 필요.

3. 색깔

   참고사이트

   - 이름 기준 : https://www.w3.org/TR/css-color-3/
   - 상세한 색상 : https://htmlcolorcodes.com/
   - 파레트 : https://www.w3schools.com/colors/colors_palettes.asp

   색상 표현단위

   - HEX : #ffffff
   - RGB: rgb(0, 0, 0)
   - RGBA: rgb(0, 0, 0, 0.5)
   - HEX값은 6개의 문자(a에서 f까지)와 숫자로 이루어져있으며 웹이나 앱에서 이용하기 편리하다.
   - RGB는 0-255의 범위의 숫자들로 각각 RGB를 나타낸다.
   - RGBA와 RGB의 다른점, RGPA에는 투명도(opacity) (0~1)를 조정할 수 있는 alpha변수가 추가되어있다.

------

## 3. Box model

매우매우매우 중요함. 정렬, 포지셔닝을 할 때 활용된다. 크롬의 개발자 도구를 보면 css를 시각화해주며 css를 수정할 수 있게 해준다. 때문에 박스모델의 margin padding border의 개념을 배우기 쉽다.

1. box model의 구성

   - Content: 실제 내용이 위치

   - Padding

     테두리 안쪽의 내부 여백, 요소에 적용된 배경의 컬러, 이미지는 패딩까지 적용

   - Border : 테두리 영역

   - Margin

     : 테두리 바깥의 외부 여백 배경색을 지정할 수 없다.

2. 기본 박스모델 활용

   1. margin

      ```css
      .margin-0{
          margin-top: 10px;
          margin-right: 20px;
          margin-bottom: 30px;
          margin-left: 40px;
      }
      
      .margin-1{
          margin: 10px;
      }
      .margin-2{
          margin: 10px 20px;
      }
      .margin-3{
          margin: 10px 20px 30px;
      }
      .margin-4{
          margin: 10px 20px 30px 40px;
      }
      ```

      margin-0은 일일이 지정해준경우, 1부터는 shorthand 버전이다. 1은 상하좌우 모두 10픽셀, 2는 상하는 10픽셀 좌우는 20픽셀, 3은 상은 10픽셀 좌우는 20픽셀 하는 30픽셀, 4는 각각 상하좌우이다.

   2. padding

      ```css
      .margin-padding{
          margin: 10px;
          padding: 30px;
      }
      ```

      이때 margin-padding은 클래스의 이름이다. padding도 동일하게 적용할 수 있다.

   3. border

      ```css
      .border-1 {
          border-width: 2px;
          border-style: dashed;
          border-color: black;
      }
      .border-2 {
          border: 2px dashed black;
      }
      .border-3 {
          border: 2px 1px dashed solid black;
      }
      ```

      border도 모든 속성을 상하좌우 따로 설정 가능하지만 이때 border-style이 지정되어있지 않으면 작동하지 않는다. 또한 shorthand로 표현할 때 3처럼 여러 속성을 상하좌우 따로 설정가능할 순 없다.

3. 기타 속성들

   1. visibility

      1. visible

         해당 요소를 보이게 한다.(기본값)

      2. hidden

         해당 요소를 안 보이게 한다. 그렇지만 공간은 남아있다. 전체적인 스트럭쳐를 망가뜨리지 않음

   2. background-image: opacity로 투명도를 조정할 수 있다.

   3. Font&Text

      1. font-size

      2. font-family

      3. letter-spacing : 자간 조정

      4. text-align : 수평적인 위치 조정.  높이 조정은 못한다.

      5. white-space

         스페이스와 탭, 줄바꿈, 자동 줄바꿈 등 공백을 어떻게 처리할지 정하는 속성이다.

         https://www.w3schools.com/cssref/pr_text_white-space.asp 

         https://www.codingfactory.net/10597 

## 4. display 속성

1. **block**

   - block 레벨 요소 예

     : div, h1~h6, p, ol, ul, li, hr(가로선 태그), table, form

   - 한줄 점유

     항상 새로운 라인에서 시작하며 화면 크기 전체의 가로폭을 차지

     다음 태그를 다음 줄로 보낸다. block 레벨 요소 내에 inline 레벨 요소를 포함할 수 있다. 예 div 안에 p

   - |    margin    |
     | :----------: |
     | content area |
     |    margin    |

     보통 block은 이런 모습(h1~h6, p 등)이거나 margin 없이 content area로만(div, form 등) 이루어짐

   - block 크기 조정

     - margin, padding, height, width 모두 적용 가능해서 모양새를 쉽게 제어할 수 있기 때문에 화면 구성이나 레이아웃에 사용한다.

     - 보통 height, width 속성으로 content area의 사이즈를 조정함으로써 block의 크기를 바꿈

       (크기 조정 대상은 오직 content area. padding, borders, margins 포함x https://www.w3schools.com/cssref/pr_dim_height.asp https://www.w3schools.com/cssref/pr_dim_width.asp). 

   - block의 가로 정렬

     - margin-right: auto, margin-left: auto 활용(margin-left:auto 시 오른쪽  정렬)

     - 너비(width)를 따로 지정해주면 나머지는 margin이 되는데 이 margin 크기를 자동으로 맞춰주어 가운데 정렬 효과

     - 그렇기 때문에 엄밀히 말하면 정렬 대상은 margin 보다 안쪽인 영역(border-padding-content)

     - text-align 속성을 이용하면 margin width 크기 지정 필요없이 원래의 크기에서 text의 정렬만 바뀐다.

       https://www.w3schools.com/cssref/pr_text_text-align.asp

   - block의 수직 정렬

     - line-height 활용
     - height 값 == line-height 값
     - height 값 만큼 커진 content area 내에서 텍스트가 수직상 가운데 정렬되는 효과가 생긴다. 

   - 코드

     ```css
     div{
       height: 200px;
       width: 100px;
       margin-right: auto;
       margin-left: auto;
       display: block;
       background-color: whitesmoke;
       text-align: center;
       line-height: 150px;
       letter-spacing: 10px
     }
     ```

     

2. **inline** 

   - inline 레벨 요소 예

     - span input a strong img br select textarea button

     - 종류

       1.a 2. span 3. img 4. 스타일 도와주는 친구 strike br 5. form내부 select, textarea, button

   - 점유와 크기 조정

     - 컨텐츠의 너비만큼 점유
     - 새로운 라인에서 시작하지 않으며 문장의 중간에 들어갈 수 있다.

   - | margin | padding | content | padding | margin | 의 형태

     - inline요소는 height와 width가 auto로 설정되어있어서 컨텐츠의 크기가 inline 요소의 크기가 되기 때문에
     - width나 height 속성 설정이 반영 안됨
     - margin-top, margin-bottom, padding-top, padding-bottom 모두 적용 안됨 (크기를 바꾸고 싶으면 폰트 크기를 바꿔야한다.)
     - margin-left,right, padding-left,right 설정 가능
     - 보통 content area만 있지만 inline level 요소끼리 연속으로 사용되면 최소한의 간격 유지를 위해 좌우에 약 5px의 외부 여백이 자동으로 발생함

   - 정렬

     - 그 자체로는 text-align 적용 x 
     - 블락 레벨요소로 감싸준 다음 그 블락 레벨 요소에 text-align을 적용
     - margin left right auto를 활용한 방법도 적용 x
     - line-height 적용했을 때 해당 inline태그에 적용되는 게 아니라 감싸는 div 크기에만 영향을 줌

   - 코드

     ```css
     a {
       margin-left: 10px;
       margin-right: 10px;
       padding-left: 10px;
       padding-right: 10px;
     }
     ```

     

3. **inline-block**

   - inline 과 비교시

     - width 와 height 지정가능
     - margin padding 지정가능

   - block 과 비교시

     - 한줄을 점유하지 않고 나란히 붙을 수 있음

     - horizontal navigation 을 만드는데 활용

       https://www.w3schools.com/css/tryit.asp?filename=trycss_inline-block_nav

   - 정렬

     block레벨 요소처럼 line-height, text-align, margin-left,right auto 모두 가능(아마도)

   - 코드

     ```css
     .inline-block {
       display: inline-block;
       margin: 10px;
       height: 100px;
       width: 100px;
     }
     ```

     

4. none

   해당 요소를 화면에 표시하지 않는다. (공간조차 사라진다.)

   동적으로 서비스 구현할 대 많이 사용함

   visible: hidden과 다르다. none은 코드상에서만 보임. invisible은 공간은 남아있지만 컨텐츠만 사라지는 경우

   ```css
   .hidden{
     visibility:hidden
   }
   .none {
     display: None;
   }
   ```

@ lie-height

- line-box: 라인, 어떤 한 요소의 높이값, 한개 혹은 여러개의 인라인 요소들로 구성될 수 있는데, 각각의 라인은 line-box 라고 불린다. line-box의 높이는 자식 요소의 높이값을 기반으로 한다. 결국 브라우저는 각 인라인 요소들의 높이를 계산하고 자식의 가장 높은 곳부터 낮은 곳까지의 길이가 line-box가 되는 것이다.
- inline요소는 content-area 높이와 line-height(line-box의 높이) 높이라는 두 개의 다른 높이를 가진다.
- line-height는 baseline간의 간격이 아니다. line-height와 content-area 높이의 차이를 행간이라고 한다. 이 행간의 절반은 항상 content-area의 상단에 더하고, 나머지 절반은 하단에 더한다. 때문에 content-area 항상 line-height의 중앙에 위치한다.
- https://wit.nts-corp.com/2017/09/25/4903

## 5. Position

스마트 폰의 등장으로 종적인 동작에 대한 니즈가 커져 버티컬한 디스플레이가 많이 발전했다. 이전에는 매우 힘들었음

1. static (기본위치)

   기본적인 요소의 배치 순서에 따라 위에서 아래로(블락), 왼쪽에서 오른쪽(인라인)으로 순서에 따라 배치되며 부모 요소 내에 자식 요소로서 존재할 때는 부모 요소의 위치를 기준으로 배치된다(dom tree구조를 잘 파악해야한다).

2. relative (상대위치)

   원래 자신의 기본위치(static으로 지정되었을 때의 위치)를 기준으로 좌표 프로퍼티(top, bottom, left, right)를 사용해 위치를 이동(음수도 가능)(이동시 블락 자체가 이동한다) 특이한점은 그 다음에 생긴 애는 그 밑으로 내려오는데 relative로 이동해도 원래 있던 자리는 가지고 있는 것. 

3. absolute (절대위치)

   relative, absolute, fixed 프로퍼티가 선언되어있는 부모 요소 또는 가장 가까이 있는 조상 요소 를 기준(static 제외, 포지션을 정의안하면 무조건 static)으로 좌표 프로퍼티(top, bottom, left, right)만큼 이동한다. 만약 상위 클래스에 static만 있을 시에는 html까지 올라가 기준을 잡을 수 있다. 그래서 absolute를 이용할 경우에는 fixed relative absolute등으로 standard를 만들어줘서 움직일 영역을 잡아준다. 상대위치와 달리 자기 공간(마진 등)을 끌고 가지 않는다. 

4. fixed (고정위치)

   부모 요소와 관계없이 브라우저의 viewport(우리가 보는 화면 자체를 viewport라고 하며 하나의 절대적인 기준으로 여긴다.)를 기준으로 좌표 프로퍼티(top, bottom, left, right)을 사용하여 위치를 이동시킨다. 스크롤이 되더라도 화면에서 사라지지 않고 항상 같은 곳에 위치한다. sticky navigation으로 활용



### 실습

```html
<body>
  <div id="box0">
    <div id="box1"></div>
    <div id="box2" class="relative"></div>
    <div id="box3"></div>
    <div id="box4"></div>
    <div id="box6"></div>
    <div id="box7"></div>
  </div>
  <div id="box5" class="fixed"></div>
</body>
```

```css
div{
  height: 100px;
  width: 100px;
}
#box0 {
  position:relative;
  height: 500px;
  width: 500px;
  border: solid;
  z-index: 100;  
}
#box1 {
  background-color: pink
}
#box2 {
  background-color: blue;
  position: relative;
  left: 100px;
}
#box3 {
  background-color: green;
  position: relative;
  left: 200px
}
#box4 {
  background-color: red;
  position: relative;
  left: 400px;
  top: 100px;
}
#box5 {
  background-color: orange;
  height: 100px;
  width: 100px;
  position: fixed;
  bottom: 0px;
  right: 0px;
  z-index: 300;
}
#box6{
  background-color :yellow;
  position:relative;
  left: 200px;
  bottom: 400px;
}
#box7{
  background-color: purple;
  position:absolute;
  left: 300px;
  top: 300px;
}
```



## 6. 셀렉터

- 다같은 div이기 때문에 selector (id, class)가 필요. css의 클래스는 우리가 원하는 형태로 분류해서 쓰겠다는 뜻. class 는 . id는 #이 앞에 붙는다.

- id class 태그명 등 각각 설정이 되어있을 때 우선순위는 id class 태그명 순이다. 날 상세하게 지칭할 수록 더 우선순위. important는 가장 높은 우선순위  부여

- 자식 후손 셀렉터

  ```css
  ol>li {
      color: black;
  }
  
  ol li {
      color: black;
  }
  ```

  - 후손 선택자는 문서구조에서 특정 요소의 자손을 선택하는 선택자로 자손은 자식, 손자, 이후의 모든 후손을 포함한다. 공백으로 분리하여 표시
  - 자식 선택자는 특정요소의 직계자식만 선택하며 자식 이후 손자, 후손들은 포함하지 않는다.

  ```css
  ol>li:nth-last-child(1) {
      color: rosybrown
  }
  ol>li:nth-child(6) {
      color: rosybrown
  } 
  #ssafy> h2:nth-child(1) {
      color : red;
  } 
  #ssafy > p:nth-of-type(2) {
      color: blue;
  }
  ```

  - : nth-child(n)

    : selector to select the element that is the *n*th child, **regardless of type**, of its parent.

    #ssafy>p: nth-child(1) 이라고 했는데 ssafy의 첫번째 자식 요소가 p가 아니면 적용되지 않는다.

  - :nth-of-type(n)

    : selector matches every element that is the *n*th child, of a particular type, of its parent.

    #ssafy>p: nth-child(1) 이라고 했을 때 ssafy의 자식 중 p태그들 중 첫번째에 적용된다.

### 기타

- 더미텍스트 더미 이미지

  lorem pixel
  lorem ipsum
  더미테스트 더미이미지들을 모아둔 곳 여기서 가져올 수 있다
  표준 텍스트 모음 뚧띱빯띨ㄴ 같은

- 가상환경 설정

  파일하나 생성
  python -m venv 파일명
  deactivate를쓰면 가상환경에서 벗어남
  source 그 파일의 scripts/activate 를 쓰면 가상환경 온

- 깃배쉬 단축명령 파일

  bashrc