# HTML

- Hyper Text Markup Language = 웹 페이지를 작성하기 위한 역할 표시(태그) 언어

  어떤 특정 내용이 이 문서 안에서 어떤 역할을 하는지 표시하기 때문에 마킹이라고 한다. 태그를 통해 마킹하는데 태그를 통해 파싱하기 더 편했기 때문이다. 마크다운은 훨씬 더 간단하다.

  HTML만 볼수있게 해주는 chrome 익스텐션 web developer extension

- Hyper Text Transfer Protocol (HTTP(S))= Hyper Text를 주고받는 규칙 

  https는 secure 기능 업그레이드(암호화단계추가)했는데 http보다 가볍고 개선했으며 빠르다(해쉬값이 없기 때문에). 

- Hyper Text란 기존의 선형적인 텍스트가 아닌 비 선형적으로 이루어진 텍스트를 의미하며, 이는 인터넷의 등장과 함꼐 대두되었다. 기본적으로 HyperLink를 통해 텍스트를 이동한다. 이러한 Hyper Text는 인간이 기억하는 방식까지 바꾸고 있는데 이를 컬럼비아대 벳시 스패로 교수님은 구글 효과(Google Effect) 라고 이름 붙였다.

- HTML 파일 : HTML 로 작성된 문서파일

- Get (받다) HTML로 작성된 문서파일 단 하나를 받는 것

- 웹 표준: W3C(Word Wide Web Consortium) vs WHATWG(Web Hypertext Application Technology Working Group)

- HTML Living Standard

- mdn web docs는 교과서이다.

------

## 1. HTML문서의 기본구조

view JS에서는 !+tab으로 html 문서의 기본구조가 자동완성된다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
    <title>Document</title>
</head>
</html>
```

- **DOCTYPE 선언부** 

  사용하는 문서의 종류를 선언하는 부분 보통 html을 사용한다.

  lang="ko" : 웹접근성과 관련되어 중요. inclusive하게 만들기 위해서 꼭 해당언어로 바꿔주기

  웹 접근성이란 : https://accessibility.naver.com/ 

- **html 요소** 

  HTML문서의 최상위 요소로 문서의 root를 뜻한다. head와 body부분으로 구분된다.

- **head 요소** 

  문서 제목(title), 문자코드(인코딩)(meta charset)와 같이 해당 문서 정보를 담고 있으며, 브라우저에 나타나지 않는다.

  css 선언(style) 혹은 외부 로딩 파일 지정(link)등도 작성한다.

  Open Graph (카카오톡  등에서 링크를 올렸을 때 올라오게되는 작은 박스 형태의 미리보기)를 지정할 수 도 있다.

  ```html
  <meta property="og:title" content="Google 뉴스">
  <meta name="og:description" content="Google 뉴스가 전세계 매체로부터 종합한 최신 뉴스">
  <meta property="og:site_name" content="Google 뉴스">
  <meta property="og:url" content="https://news.google.com">
  <meta propety="og:type" content="website">
  <meta property="og:image" content="https://lh3.googleusercontent.com/J6_coFbogx"
  ```

- **body요소**

  브라우저 화면에 나타나는 정보로 실제 내용에 해당한다.

------

## 2. Tag와 DOM TREE (Document Object Model)

브라우저는 태그들을 하나의 객체처럼 받는다. 

0. **주석**

   ```html
   <!--주석내용-->
   ```

1. **요소(Element)**

   HTML의 요소는 태그와 내용(contents)로 구성되어 있다.

   ```html
   <h1> contents </h1>
   ```

   태그는 대소문자를 구별하지 않으나, 소문자로 작성해야 한다. 요소간의 중첩도 가능하다.

2. **self-closing element**

   <img src=""/>

   닫는 태그가 없는 태그. 표시할 내용이 없기 때문이다. 

   img태그에서 alt속성은 엑박뜰 경우 쓸 내용을 넣는다.(표준이며 접근성을 위해, ex) 인스타그램, vpqnr)

3. **속성(Attribute)**

   <a href="https://google.com"/>

   여기서 href는 속성명이고, "주소"는 속성값이다. 

   <(여는) 태그 속성명="속성값">의 형식

   태그에는 속성이 지정될 수 있으며, id, class, style 속성은 태그와 상관없이 모두 사용 가능하다.

   속성과 속성값 사이에는 공백이 없어야하며, 속성값은 큰따옴표로 감싸줘야한다.

4. **DOM 트리**

   ```html
   <body>
      <h1>웹문서</h1>
       <ul>
           <li>HTML</li>
           <li>CSS</li>
       </ul>
   </body>
   ```

   태그는 중첩되어 사용가능하며, 이때 다음과 같은 관계를 갖는다.

   최상단의 태그는 html, 아래 태그들과 계층구조를 이룬다.

   body 태그와 h1태그는 부모(parent)-자식(child) 관계

   h1태그와 ul태그는 형제관계(sibling)

   구조는 TAB(2 space)로. 구조를 통해 웹에서 의도한대로 작동하며 검색될 수 있다.

5. **시맨틱 태그(Semantic Tag)**

   `<div>` `</div>`태그는 division, 공간을 분할 할 뿐 의미는 없다. display:block을 지정하기 위한 기본 레이아웃 태그

   시맨틱 태그는 의미가 있는 태그

   HTML5에서 새롭게 지정된 시맨틱 태그의 일부

   | 태그    | 설명                                                         |
   | ------- | ------------------------------------------------------------ |
   | header  | 헤더 (문서 전체나 섹션의 헤더)                               |
   | nav     | 내비게이션                                                   |
   | aside   | 사이드에 위치한 공간으로, 메인 콘텐츠와 관련성이 적은 콘텐츠에 사용 |
   | section | 문서의 일반적인 구분으로 콘텐츠 그룹을 표현하며, 일반적으로 h1~h6 요소를 가짐 |
   | article | 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역(포럼/신문 등의 글 또는 기사) |
   | footer  | 푸터(문서 전체나 섹션의 푸터)<br />(보통 날씨 등 특정 요소를 지정할 때, 또는 아래 쪽 요소들을 표현할 때, 안내고객센터 등 회사 정보들이 나와있다, 의미 단위로 묶어준다?) |

   개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미있는 정보의 그룹을 태그로 표현하여 단순히 보여주기 위한 것을 넘어서 의미를 가지는 태그들을 활용하기 위한 노력

   non semantic 요소: div, span 등

   검색 엔진 최적화 (SEO, search engine optimization)가 중요한 이유는 user base service에서 서비스가 유저들에게 잘 발견되기 위해서

   검색할 때 뜨는 것은 title

   view JS에서 tab = 2space로 설정해 주기 위해서 beauty라는 extension으로 설정 또는 페이지 단위로 스페이스 설정

------

## 실습

1. list의 bullet 모양을 바꿔보기

   ```python
   <li style="list-style-type:circle">HTML</li>
   ```

   list-style-type의 속성값: none, square, circle, lower-alpha, upper-alpha, upper-roman

   shortcut : ol>li*4

   strike 태그(= s 태그, 취소선), del 태그(취소선), b 태그(볼드), em 태그(강조, 이탤릭), i태그(이탤릭체) 등

   인라인 요소들을 지정할 때 block base tag 인 p 태그로 감싸주면 해당 가로공간 전체를 차지 하기 때문에 구획을 의미별로 나눌 수 있다.

   반면 컨텐츠 만큼의 공간만 차지하는 태그를 inline 태그라고 한다. 예를 들어 span태그는 p태그 처럼 글을 감싸줄 때 쓸 수 있지만 inline base tag이다. span태그로 감싸인 글 부분들은 한 줄에 이어서 써지기 때문에 br태그를 이용해 다음 줄로 넘길 수 있다. 

   03_markup.html

2. 하이퍼링크

   03_markup.html

3. section 에 id값을 지정하고 각 항목 또는 같은 폴더내의 다른 파일로 이동하기

   ```html
   <a href="#python">파이썬으로가기</a>
   <section id="python">
   	<h3>
           파이썬 입니다.
       </h3>
   </section>
   ```

   03_markup.html

4. a tag에 있었던 내용을 이미지로 대체하기(images 폴더에 넣어서 활용)

   ```html
   <a href="#python"><img src="주소"></a>
   ```

5. 영상 넣기

   ```html
   <iframe width="420" height="315"
   	src="https://www.youtube.com/embed/tgbNymZ7vqY">
   </iframe>
   ```

6. table 태그를 활용하기 

   table 태그에서 중요한 건 행이기 때문에 처음에 tr태그를 쓰며 그 안에 들어가는 데이터(열)을 넣기 위해 td 태그

   tr: table row td: table data th: table head(보통 첫줄)

   ```html
   <table>
       <tr>
         <th></th>
         <th>월</th>
         <th>화</th>
         <th>수</th>
       </tr>
       <tr>
           <td>A코스</td>
           <td rowspan='2'>짬뽕</td>
           <td colspan='2'>초밥</td>
       </tr>
       <tr>
           <td>B코스</td>
           <td>김치찌개</td>
           <td>삼계탕</td>
       </tr>
     </table>
   ```

   첫번째 tr태그는 첫번째 줄, 다음 tr태그는 두번째 줄. 첫째 줄의 각 열은 th로 감쌌다.빈칸으로 두면 빈 열로 생김.

   만약 행 통합을 하고 싶을때는 rowspan="통합하고 싶은 연속된 열의 수"로 속성과 속성값을 주면되며, 열 통합을 하고 싶으면 colspan="통합하고 싶은 연속된 행의 수". 이때 다음열이나 행을 작성할 때는 통합된 부분은 넘어가고 다음 부분부터 작성 

   스타일은 각 요소마다 지정해 줄 수 있다.

   ```html
   <style>
       table, tr, td, th{
           border: 1px solid black
       }
   </style>
   ```

   04_lunch.html

   05_festival.html

   

7. form 태그 활용하기

   - 이름과 날짜 작성(input type="text", "datetime")

     ```html
     <form action="">
         <span>이름: <input type="text" placeholder="이름을 입력해주세요"></span><br>
         <span>날짜: <input type="datetime" value="2019. 01. 03." size="25"></span>
     </form>
     ```

     input 태그의 속성 type은 입력값의 타입 지정, placeholder 는 미리보기, value는 디폴트 값 지정

     type 속성의 속성값 중 date는 직접 달력에서 골라 url에 파라미터로 vs  datetime은 string의 느낌

   - 샌드위치 선택하기(input type="radio")

     ```html
     <span><input type="Radio" Name="sandwich" Value="egg">에그마요</span><br>
     <span><input type="Radio" Name="sandwich" Value="bmt">이탈리안 비엠티</span><br>
     <span><input type="Radio" Name="sandwich" Value="avo">터키 베이컨 아보카도</span><br>
     ```

     input 태그의 type 속성의 Radio값으로 지정해주면 사용자가 선택한 것을 value속성의 값으로 받을 수 있다. 

   - 사이즈 선택하기(input type="number")

     ```html
     <input type="number" min="15" max="30" size="3">    
     ```

     input 태그의 type 속성의 number값일 때 최소 최대값을 지정해 줄 수 있다. size는 왜 저렇게 해둔거지? 

   - 빵 선택하기(드랍다운)(select태그, option태그)

     ```html
         <h2>3. 빵</h2>
           <select name="bread">
             <option value="" disabled selected>Select</option> 
             <option Value="1">허니오트</option>
             <option Value="2" disabled>플랫브래드</option>
             <option Value="3">하티 이탈리안</option>
           </select>
     ```

     select의 name값을 설정해줘야하는 이유는 option태그의 value속성값이 설정되었을 때 select 태그의 name으로 value의 속성값이 넘어가기 때문이다. 아마 name=value 이런식으로. 보통 value를 숫자로 설정해 값이 넘어가며 숫자와 빵이 연결되게..?

   - 야채 소스 선택(checbox)(input type="checkbox")

     ```html
     <span><input type="Checkbox" Name="야채/채소" Value ="토마토">토마토</span><br>
     <span><input type="Checkbox" Name="야채/채소" Value ="오이">오이</span><br>
     <span><input type="Checkbox" Name="야채/채소" Value ="할라피뇨">할라피뇨</span><br>
     <span><input type="Checkbox" Name="야채/채소" Value ="핫 칠리">핫 칠리</span><br>
     <span><input type="Checkbox" Name="야채/채소" Value ="바베큐">바베큐</span><br>
     ```

   - 제출하기(button type="submit")

     ```html
     <button type="submit">submit</button>
     ```

     

   어떻게 동작하는지 모르겠다. 아마도 form태그 안에서 button이 동작하게되면 입력된 input값들이 form 태그의 action 속성 값에 적힌 주소로 제출되는 것..?

   06_form.html

   게시판 같은 곳에서 form 을 많이 사용함