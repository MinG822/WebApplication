# bootstrap

build responsive, mobile-first projects on the web with the world's most popular front-end component library. bootstrap is an open source toolkit for developing with HTML, CSS, and JS.

Bootstrap vs Material

Bootstrap 으로 만든 사이트들, 같은 듯 다른 bootstrap

bootstrap은 html에서 정의한 스타일과 달리 bootstrap만의 새로운 스타일을 적용한다. 예를 들어서 위아래로 16px정도의 마진이 있는 원래의 h1과 달리 bootstrap의 h1은 아래마진만 8px정도 있다. 마진 콜랍싱을 제거하기 위해서 

------

## quick start

cdn 활용을 통해 bootstrap에 작성된 css, js를 활용하자

### CDN이란?

- Content Delivery(Distribution) Network
- 컨텐츠(Css, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템
- 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점) 외부서버를 활용함으로써 본인 서버의 부하가 적어짐 CDN은 보통 적절한 수준의 캐시 설정으로 빠르게 로딩할 수 있음.

### 시작하기 전에 CSS reset

1. Utilities

   1. spacing

      - .m-0?

      ```css
      .m-0 {
      	margin: 0 !important;
      }
      ```

      - .mr-0?

        ```css
        .mr-0 {
        	margin-right: 0 !important;
        }
        ```

      - .mx-0?

        ```css
        .mx-0 {
        	margin-right: 0 !important;
            margin-left: 0 !important;
        }
        ```

      - .py-0?

        ```css
        .py-0 {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }
        .px-0 {
            padding-right: 0 !important;
            padding-left: 0 !important;
        }
        ```

      - .mt-1?

        ```css
        .my-1 {
        	margin-top: 0.25rem !important;
        }
        ```

        spacer(1rem)*0.25 = 16px * 0.25 = 4px (브라우저 기본 rem은 16px)

        mt-2 = 0.5 rem = 8px

        mt-3 = 1 rem = 16px

        mt-4 = 1.5 rem = 24px

        mt-5 = 3 rem = 48px

      - m = margin, p= padding

        t = top, b= bottom, l=left, r=right, x=left,right, y=top,bottom

        0=0px, 1=0.25rem=4px, 2=0.5rem=8px, 3=1rem=16px, 4=1.5rem=24px, 5=3rem=48px

        음수도 가능

      - .mx-auto?

      css를 정의할 때  위아래 위치로 인해 차이가 생길까? 예를 들어 mr-0을 정의하고 밑에 mx-0을 정의하면? 둘다 important가 걸려있으면? 뭐가 더 우선시 될까?

   2. Color

      primary secondary success info warning danger light dark white transparent

      background-color: primary (color생략가능) -> class=".bg-primary"

      글자색 변경: .text-success

      형광펜 효과: .alert-warning 

      버튼 만들기: .btn-secondary

      활용: .navbar-dark .bg-primary

   3. border

      spacing을 활용하면 Box model 설정이 끝 .border-

      색상과의 조합도 가능 .border-success

   4. radius

      .rounded-

      rounded-circle, rounded-pill

   5. display

      Box model.. display까지?

      display: block -> .d-block .d-inline .d-none .d-inline-block .d-table

      .d-sm-none?

      breakpoint들

      |                     | Extra small | Small | Medium | Large | Extra Large |
      | ------------------- | ----------- | ----- | ------ | ----- | ----------- |
      | Max container width | None(auto)  | 540px | 720px  | 960px | 1140px      |
      | Class prefix        |             | sm    | md     | lg    | xl          |

   6. position

      Box model.. position 까지?

      position: static -> .position-static

      .position-relative

      .postion-absolute

      .postion-fixed

      .fixed-top

      .fixed-bottom

   7. Text

      글자변경도 자유롭게!

      text-align: center -> .text-center, .text-left, .text-right

      font-weight: bold -> .font-weight-bold, .font-weight-border, .font-italic

   8. Components 는 공식문서로 확인



------

## 그리드 시스템

bootstrap은 스페이싱을 편리하게 해준다.

그리드 시스템 항상 컨텐츠 배치를 횡적으로 해줘라. 그러니까 횡적인 여백들이 양옆에 있는 공간. 횡들을 쌓아올라가는 느낌으로.
반응형단점,. 컨텐츠가 어디로 갈지 모른다. 그래서 네이버는 반응형이아니라 모바일형을 새로 만든다. 작은 모니터(1100px)를 쓰는 사람들도 배려하기 위해서. 그래서 부트스트랩 컨테이너도 크기가 제한이 있는 것이다. 그게 싫으면 container-fluid를 쓰면 된다.(그러면 캐러셀은 container-fluid로 나머지는 container로 쓰면 된다!)

플렉스를 이용한 디스플레이. row라는 공간의 뜻은 flex박스

그리드 사이에 공간을 주고 싶으면 마진을하는게 하니라 패딩. 남을 미는게 아니라 나를 줄여야한다.
반응형이라는 것은 row로 펼쳐놓은 애들을 디바이스크기가 줄어듬과 동시에 모바일 기준으로 수직으로 쌓아야한다. css의 요소 중 크기가 줄어드는 것을 감지하는 것을 이용하는데, 부트스트랩을 사용하면 더 편하다. 디바이스의 크기를 적어주면 됨. div class col-sm-4 로 쓸 수 있다. 이러면 작은 사이즈로 볼 때 이 컨텐츠를 풀어준다는 뜻이다 한줄에 이 컨텐츠만 있게. 이게 브레이크 포인트. 

