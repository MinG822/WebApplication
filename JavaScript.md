# JavaScript

[TOC]



## 1. 기본 문법

### 1. 변수  `var`,` let`, `const`

| `var`          | `let`                | `const`            |
| -------------- | -------------------- | ------------------ |
| function scope | block scope          | block scope        |
| 재선언 가능    | 재선언 불가능        | 재선언 불가능      |
| 재할당 가능    | 재할당 가능          | 재할당 불가능      |
|                | 선언시 초기값 불필요 | 선언시 초기값 필요 |

```javascript
// 블록 스코프 - let, const
for(var j=0; j<1; j++) {
  console.log(j)
}
console.log(j)

for(let i=0; i<1; i++) {
  console.log(i)
}
console.log(i)

//함수 스코프 - var
const myFunction = function () {
  for (var k=0; k<1; k++) {
    console.log(k)
  }
  console.log(k)
}
myFunction()
console.log(k)

// var 재선언 가능, let, const 재선언 불가능
var a = 1
var a = 2

let b = 1
let b = 3 
// Uncaught SyntaxError: Identifier 'b' has already been declared

const c = 1
const c = 4
// Uncaught SyntaxError: Identifier 'c' has already been declared

// let 재할당 가능, const 불가능
let d = 3
d = 5

const e = 5
e = 3
// Uncaught TypeError: Assignment to constant variable.

const f
// Uncaught SyntaxError: Missing initializer in const declaration
// const 는 선언시 반드시 할당이 필요

let g
g = 3

```

*참고) 변수 선언 키워드를 사용하지 않을 시 함수/블록 안에서 선언되더라도 무조건 전역 변수로 취급된다.*

```javascript
function myFunction1 () {
  for (p=0; p<1; p++) {
    console.log(p)
  }
  console.log(p)
}
myFunction1()
console.log(p)
console.log(window.p)
```

------

### 2. 자료형

```javascript
// primitive - Boolean, null, undefined, number, string
// Object - array, object
```



------

### 3. 조건 / 반복

- if/ else if/ else

  ```javascript
  // 최소 값 구하기 (Function)
  // 기본함수 && 조건문
  // 함수의 매개변수로 두개의 숫자를 받아 그 중 낮은 수를 반환하는 함수를 만들기
  const getMin = (a, b) => {
      if (a > b) {
          return b
      }
      return a
  }
  
  const getMin2 = (a, b) => {
      let min
  // const 는 선언시 초기값이 필요하지만 let은 필요없다.
      if (a > b) {
          min = b
      } else {
          min = a
      }
      return min
  }
  
  console.log(getMin2(2, 5))
  
  // 배열을 받아서 해당 배열에서 가장 낮은 수를 반환하는 함수
  const getMinFromArray = (nums) => {
      let min = Infinity;
      // Infinity의 타입은 Infinity이다.
      // console.log(Infinity)
      nums.forEach(num =>{
          if (min > num) {
              min = num
          }
      })
      return min
  }
  
  console.log(getMinFromArray([1, 2, 3, 4]))
  ```

- while/ for/ for of

  ```javascript
  let i = 0
  while (i<10) {
      // console.log(i)
      i++
  }
  for (let j=0; j < 10; j++) {
      // console.log(j)
  }
  
  for (let number of [1, 2, 3, 4, 5]) {
      // console.log(number)
      // console.log(number=1)
  }
  
  for (const number of [1, 2, 3, 4, 5]) {
      // console.log(number)
      // console.log(number=1) const 는 재할당 불가
  }
  ```

  - 참고

    > ```javascript
    > for (variable of iterable) {
    >   statement
    > }
    > ```
    >
    > - `variable`
    >
    >   On each iteration a value of a different property is assigned to `variable`. `variable` may be declared with `const`, `let`, or `var`.
    >
    >   ```
    >   iterable
    >   ```
    >
    >   Object whose iterable properties are iterated.



---

### 4.배열 Array (Object)

```javascript
const numbers = [1, 2, 3, 4];

numbers[0] //1
numbers[-1] //undefined
numbers.length //4

numbers.reverse() // [4, 3, 2, 1]
numbers // [4, 3, 2, 1]

numbers.push('a') // 5 (new length)
numbers // [1, 2, 3, 4, 'a']

numbers.pop() // 'a'
numbers // [1, 2, 3, 4]

numbers.unshift('a') // 5
numbers // ['a', 1, 2, 3, 4]

numbers.shift() // 'a'
numbers // [1, 2, 3, 4]

numbers.includes(1) // true
numbers.includes(0) // false

numbers.push('a') // 5
numbers.push('a') // 6
numbers // [1, 2, 3, 4, 'a', 'a']
numbers.indexOf('a') // 4 처음찾은 요소의 index
numbers.indexOf('b') // -1 없을시

numbers.join() // '1,2,3,4,a,a'
numbers.join('') // 1234aa
numbers.join('-') // '1-2-3-4-a-a'

numbers // [1,2,3,4,'a','a']

typeof numbers // object
```



------

### 5. Object

- key-value로 이루어진 데이터 구조

  ```javascript
  const endGame = {
    title: '어벤져스: 엔드게임',
    my-lovers: [
      {name: '아이언맨', actor: '로다주'},
      {name: '헐크', actor: '마크 러팔로'}
    ]
  }
  
  endGame.title
  endGame['title']
  endGame['my-lovers'][0].name
  ```

- Object Literal (ES6+)

  ```javascript
  const comics = {
    'DC': ['Aquaman', 'SHAZAM'],
    'Marvel' : ['Captain Marvel', 'Avengers']
  }
  const magazines = null
  
  const bookShop = {
    comics,
    magazines,
  }
  ```

  - 참고) literal이란

    >  In computer science, a **literal** is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. 

- method

  파이썬과 달리 별도의 문법이 있는 것이 아니라 오브젝트의 value에 함수를 할당 한다.

  ```javascript
  const me = {
    name: 'Kim',
    greeting: function(message) {
      return `${this.name} : ${message}`
    }
  }
  me.greeting('hi') // Kim : hi
  me.name = 'John'
  me.greeting('hello') // John : hello
  ```

  앞선 변수/object 와 같이 함수도 ES6+ 부터 아래와 같이 선언 가능하다.

  ```javascript
  const greeting = function(message) {
      return `$(this.name} : ${message}`
  }
  
  const you = {
      name: 'Yu',
      greeting,
      bye() {
          return 'bye'
      }
  }
  
  you.greeting('hi') // Yu : hi
  you.name = 'Jane'
  you.gretting('hello') // Jane : hello
  you.bye() // bye
  ```

  *참고) 메서드 정의시, `arrow function`을 사용하지 않는다.*

---

### 6. JSON

> key - value 형태의 자료구조를 JS Object와 유사한 모습으로 표현하는 표기법. 모습만 비슷할 뿐이고 실제로 Object 처럼 사용하려면 다른 언어들처럼 JS 에서도 Parsing(구문분석) 작업이 필요하다.

```javascript
//Object => JSON

const jsonData = JSON.stringify({
    coffee: 'Americano',
    iceCream: 'Cookie and cream',
})

console.log(jsonData)
// json 변환시 키 값과 string 값은 모두 쌍따옴표 표기
console.log(typeof jsonData)

const fs = require('fs')
// 파일 생성
fs.writeFile('me.json', meJSON, err => {})
fs.writeFileSync('me2.json', meJSON)

// string

//Json => Object
const parseData = JSON.parse(jsonData)
console.log(parseData)
console.log(typeof parseData)
```



---

### 7. 함수

```javascript
// 함수 선언식
function myFunc1 (name) {
    console.log('happy hacking')
    console.log(`welcome, ${name}`)
}

// 함수 표현식
const myFunc2 = function (name) {
    console.log('happy hacking')
    console.log(`welcome, ${name}`)
}

typeof myFunc1 // function
typeof myFunt2 // function

// arrow 함수 (ES6+)

const myFunc3 = (name) => {
    console.log('happy hacking')
    console.log(`welcome, ${name}`)
}

// Anonumous function (익명/1회용 함수)
console.log((function (num) { return num**3})(2))
console.log((num => num**0.5)(4))
```



#### 참고1) arrow function & this

> Arrow function
>
>  An arrow function does not have its own `this`. The `this` value of the enclosing lexical scope is used; arrow functions follow the normal variable lookup rules. So while searching for `this` which is not present in current scope, an arrow function ends up finding the `this` from its enclosing scope.
>
>  [출처 : mdn](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

- arrow 함수는 function 키워드로 정의한 위의 함수와 100% 동일한 것이 아님. this 키워드가 등장하게 되면, 둘은 다르게 동작한다. 

- arrow function은 별도의 지정없이 this가 자동적으로 해당 스코프의 함수를 가리키게된다.

  ```javascript
  function Person(){
      this.age = 0;
  
      setInterval(() => {
          this.age++; // |this| properly refers to the Person object
      }, 1000);
  }
  ```

#### 참고2) syntactic sugar

```javascript
let square = function (num) {
    return num ** 2
}

// 인자가 하나 일 때 괄호를 생략해도 된다.
square = num => {
    num ** 2
}

// 인자가 없을 때는 괄호를 반드시 써줘야한다.
const sayHello = () => 'hello'

// 기본인자를 줄 때는 인자 갯수와 상관없이 꼭 괄호를 해야한다.
const sayHello2 = (name='anonymous') => `hello ${name}`

// 표현식이 한 줄 이면 중괄호를 생략해도된다.
square = num => num ** 2

// object를 반환한다면 괄호를 써줘야한다.
// 괄호를 안하면 함수블록으로 인식
let returnObject = () => { return { key: 'value'}}
returnObject = () => ({ket:'value'})

```

---

### 8. Array Helper Methods

- forEach

  ```javascript
  //forEach forEach 함수는 아무것도 return 하지 않는다.
  // ES6+
  const colors = ['red', 'blue', 'green']
  colors.forEach(function(color) {
      console.log(color)
  })
  console.log(typeof colors)
  // Array 의 타입은 object이다.
  // forEach 뒤에 오는 익명함수를 callback function이라고 부른다.
  colors.forEach(color => {
      console.log(color)
  })
  //Exercise
  const images = [
      {height: 10, width: 30},
      {height: 20, width: 90},
      {height: 54, width: 32},
  ]
  
  const areas = [];
  
  images.forEach(function (image) {
      areas.push(image.height*image.width)
      console.log(areas)
  })
  
  // const areas에 push하는 것은 괜찮지만 areas=[] 를 하면 TypeError: Assignment to constant variable.
  
  images.forEach(image => {
      areas.push(image.height*image.width)
      console.log(areas)
  })
  ```

- map

  ```javascript
  // map 함수는 새로운 배열을 return한다. 그래서 const doubleNumbers에 할당가능
  
  const numbers2 = [1, 2, 3]
  
  const doubleNumbers = numbers2.map(function(number) {
      return number * 2
  })
  console.log(doubleNumbers)
  
  // exercise1
  
  // const heights 초기값을 설정하지 않으면 SyntaxError: Missing initializer in const declaration
  
  const heights = images.map(function(image) {
      return image.height
  })
  
  console.log(heights)
  
  // exercise2
  
  // map 헬퍼를 사용해서, distance/time(속도) 를 저장하는 배열 speeds를 만들기
  
  const trips = [
      {distance: 34, time: 10},
      {distance: 90, time: 50},
      {distance: 59, time: 25},
  ]
  
  const speeds = trips.map(trip => {
      return trip.distance/trip.time
  })
  
  console.log(speeds)
  
  // exercise3
  function pluck (array, property) {
      return array.map(temp => {
          return temp[property]
      })
  }
  
  const paints = [
      { color: 'red'},
      { color: 'blue'},
      { color: 'yellow'}
  ]
  
  console.log(pluck(paints, 'color'))
  ```

- filter

  ```javascript
  //filter 해당 조건문에서 true를 만족하는 필터링된 요소들만 있는 배열로 return 한다.
  
  const products = [
      {name:'cucumber', type:'vegetable'},
      {name:'banana', type:'fruit'},
      {name:'carrot', type:'vegetable'},
      {name:'apple', type:'fruit'}
  ]
  
  const fruitProducts = products.filter(function(product) {
      return product.type === 'fruit'
  })
  console.log(fruitProducts)
  
  const fruitProducts2 = products.filter(product => {
      return product.type === 'fruit'
  })
  console.log(fruitProducts2)
  console.log(typeof fruitProducts)
  
  //exercise
  const numbers3 = [10, 20, 30];
  
  function reject(array, iteratorFunction) {
      return array.filter(function(element) {
          return !iteratorFunction(element)
      })
  }
  
  const lessThan15 = reject(numbers3, function(number) {
      return number > 15
  })
  
  console.log(lessThan15)
  ```

- find

  ```javascript
  //find 함수는 찾은 요소 한가지만 return 한다.
  
  const users = [
      {name: 'Tony Stark'},
      {name: 'Steve Rogers'},
      {name: 'Thor'},
      {name: 'Tony Stark'},
  ]
  
  console.log(users.find(user => {
      return user.name === 'Tony Stark'
  }))
  // { name: 'Tony Stark' }
  
  const tony = users.find(user => {
      return user.name === 'Tony Stark'
  })
  
  console.log(tony)
  
  console.log(users.filter(user => {
      return user.name === 'Tony Stark'
  }))
  
  // exercise
  
  const ladders = [
      {id: 1, height: 20},
      {id: 3, height: 25},
  ]
  
  function findWhere(array, criteria) {
      const property = Object.keys(criteria)[0]
      // criteria라는 오브젝트의 키값이 배열로 나오는데 첫번째값을 property에 저장한다.
      return array.find(function(temp) {
          return temp[property] === criteria[property]
      })
  }
  console.log(findWhere(ladders, {height:20}))
  ```

  - 참고) node의 전역 객체는 ?

    ```javascript
    // node의 전역객체는 global
    Object.keys(global)
    /*[
        'global',
        'clearInterval',
        'clearTimeout',
        'setInterval',
        'setTimeout',
        'queueMicrotask',
        'clearImmediate',
        'setImmediate'
        ]
    */
    ```

- every & some

  ```javascript
  // every & some
  // every와 some은 기존처럼 대상 배열에서 특정요소를 뽑거나 배열을 return하지않고, 조건에 대해 boolean값을 return한다.
  
  const computers = [
      { name: 'macbook', ram: 16 },
      { name: 'gram', ram: 8 },
      { name: 'series9', ram: 32 },
  ]
  
  // (computers[0] >16 ) && (computers[1] >16 ) && (computers[2] >16)
  const everyComputerAvailable = computers.every(computer => {
      return computer.ram > 16
  })
  
  // (computers[0] >16) || (computers[1]>16) || (computers[2]>16)
  const someComputerAvailable = computers.some(computer => {
      return computer.ram > 16
  })
  
  console.log(everyComputerAvailable, someComputerAvailable)
  
  // exercise
  const users2 = [
      { id: 21, hasSubmitted: true},
      { id: 33, hasSubmitted: false},
      { id: 712, hasSubmitted: true},
  ]
  
  const everySubmitted = users2.every(user => {
      return user.hasSubmitted
  })
  
  console.log(everySubmitted)
  
  // exercise2
  const requests = [
      { url: '/photos', status: 'complete'},
      { url: '/albums', status: 'pending'},
      { url: '/users', status: 'failed'},
  ]
  
  const inProgress = requests.some(temp => {
      return temp.status === 'pending'
  })
  
  console.log(inProgress)
  ```

- [reduce](https://www.zerocho.com/category/JavaScript/post/5acafb05f24445001b8d796d)

  `배열.reduce((누적값, 현잿값, 인덱스, 요소) => { return 결과 }, 초깃값)`

  ```javascript
  // 덧셈예시
  result = oneTwoThree.reduce((acc, cur, i) => {
    console.log(acc, cur, i);
    return acc + cur;
  }, 0);
  // 0 1 0
  // 1 2 1
  // 3 3 2
  result; // 6
  
  // 초깃값을 적어주지 않으면 자동으로 초깃값이 0번째 인덱스의 값이 됩니다.
  
  result = oneTwoThree.reduce((acc, cur, i) => {
    console.log(acc, cur, i);
    return acc + cur;
  });
  // 1 2 1
  // 3 3 2
  result; // 6 
  
  // map을 reduce로 구현하기
  result = oneTwoThree.reduce((acc, cur) => {
    acc.push(cur % 2 ? '홀수' : '짝수');
    return acc;
  }, []);
  result; // ['홀수', '짝수', '홀수']
  
  //초깃값을 배열로 만들고, 배열에 값들을 push하면 map과 같아집니다. 이를 응용하여 조건부로 push를 하면 filter와 같아집니다. 다음은 홀수만 필터링하는 코드입니다.
  
  result = oneTwoThree.reduce((acc, cur) => {
    if (cur % 2) acc.push(cur);
    return acc;
  }, []);
  result; // [1, 3]
  
  // 비동기 프로그래밍
  const promiseFactory = (time) => {
    return new Promise((resolve, reject) => {
      console.log(time); 
      setTimeout(resolve, time);
    });
  };
  [1000, 2000, 3000, 4000].reduce((acc, cur) => {
    return acc.then(() => promiseFactory(cur));
  }, Promise.resolve());
  // 바로 1000
  // 1초 후 2000
  // 2초 후 3000
  // 3초 후 4000
  
  //반복되는 모든 것에는 reduce를 쓸 수 있다는 것을 기억하시면 됩니다.
  ```

  

---

## 2. DOM

### 1. Event Listener 구분

| Event Listener | 설명                                                         |
| -------------- | ------------------------------------------------------------ |
| click          | 마우스버튼을 클릭하고 버튼에서 손가락을 떼면 발생한다        |
| mouseover      | 마우스를 HTML요소 위에 올리면 발생한다.                      |
| mouseout       | 마우스가 HTML요소 밖으로 벗어날 때 발생한다.                 |
| mousemove      | 마우스가 움직일때마다 발생한다. 마우스커서의 현재위치를 계속기록하는 것에 사용할 수 있다. |
| keypress       | 키를 누르는 순간에 발생하고 키를 누르고 있는 동안 계속해서 발생한다. |
| keydown        | 키를 누를 때 발생한다.                                       |
| keyup          | 키를 눌렀다가 떼는 순간에 발생한다.                          |
| load           | 웹페이지에서 사용할 모든 파일의 다운로드가 완료되었을 때 발생한다. |
| scroll         | 스크롤바를 드래그하거나 키보드(up, down)를 사용하거나 마우스 휠을 사용해서 웹페이지를 스크롤 할 때 발생한다. 페이지에 스크롤바가 없다면 이벤트는 발생하지 않는다. |
| change         | 폼 필드의 상태가 변경되었을 때 발생한다. 라디오 버튼을 클릭하거나 셀렉트 박스에서 값을 선택하는 경우를 예로 들수 있다. |
| input          | input 또는 textarea요소의 값이 변경되었을 때                 |
| submit         | form을 submit할때                                            |

---

### 2. DOM selector

- querySelector()

  -  The [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document) method `**querySelector()**` returns the first [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element) within the document that matches the specified selector, or group of selectors. If no matches are found, `null` is returned. 

  - ```javascript
    element = document.querySelector(selectors);
    ```

    selectors

    A [`DOMString`](https://developer.mozilla.org/en-US/docs/Web/API/DOMString) containing one or more selectors to match. This string must be a valid CSS selector string; if it isn't, a `SYNTAX_ERR` exception is thrown. 

  - ```javascript
    // select query by ID
    const el = document.querySelector( "#main, #basic, #exclamation" )
    ```

- querySelectorAll()

  -  The [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element) method `**querySelectorAll()**` returns a static (not live) [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) representing a list of elements matching the specified group of selectors which are descendants of the element on which the method was called. 

  - ```javascript
    elementList = parentNode.querySelectorAll(selectors);
    ```

  - return value

     A non-live [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) containing one [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element) object for each descendant node that matches at least one of the specified selectors 

  - ```javascript
    // select paragraph elements whose class is either warning or note
    const special = document.querySelectorAll( "p.warning, p.note" );
    ```

---

### 3. Event Listener 

- 특정한 `DOM elemet(무엇을)`를 `어떠한 행동을 했을 때(언제)`, `어떻게 한다.`

  ```javascript
  // 1. 무엇을
  const button = document.querySelector('#some-button')
  // 2. 언제
  button.addEventListener('click', function (event) {
      const area = document.querySelector('#my')
      // 3. 어떻게 => 뿅
      area.innerHTML = '<h1>뿅</h1>'
  })
  ```
  
- 이벤트 리스너에서의 콜백함수에는 arrow function을 사용하지 않는다. 

#### [예시 1) 공룡]( https://github.com/MinG822/WebApplication/blob/master/javascript/01_js_browser/00_dino.html )

```javascript
const dino = document.querySelector('img')

      dino.addEventListener('click', event => {
        alert('아야')
        console.log(event)
      })

      let x = 0
      let y = 0

      document.addEventListener('keydown', e => {
        console.log(e.keyCode)

        if (e.keyCode === 37) {
          console.log('왼쪽으로 이동')
          x -= 40
          dino.style.marginLeft = `${x}px`
        } else if (e.keyCode == 38) {
          console.log('위로 이동')
          y -= 40
          dino.style.marginTop = `${y}px`
        } else if (e.keyCode == 39) {
          console.log('오른쪽으로 이동')
          x += 40
          dino.style.marginLeft = `${x}px`
        } else if (e.keyCode == 40) {
          console.log('아래로 이동')
          y += 40
          dino.style.marginTop = `${y}px`
        } else {
          alert('잘못된 key를 누르셨어요. 방향키를 눌러주세요.')
        }
      })

      document.addEventListener('mousemove', e => {
        console.log(e)
      })
```



####  [예시 2) shopping list](https://github.com/MinG822/WebApplication/blob/master/javascript/01_js_browser/01_shopping_list.html)

```javascript
const input = document.querySelector('#item-input')
    const button = document.querySelector('#add-button')
    const shoppingList = document.querySelector('#shopping-list')

    button.addEventListener('click', e => {
      const itemName = input.value
      input.value = ''

      const item = document.createElement('li')
      item.innerText = itemName

      const deleteButton = document.createElement('button')
      deleteButton.innerText = 'delete'

      deleteButton.addEventListener('click', e => {
        item.remove()
      })
      
      item.appendChild(deleteButton)

      shoppingList.appendChild(item)
    })
```



---

## 3. 비동기 처리 와 Axios

### 0. 비동기처리

- [비동기처리란?]( https://joshua1988.github.io/web-development/javascript/javascript-asynchronous-operation/ )

   자바스크립트의 비동기 처리란 특정 코드의 연산이 끝날 때까지 코드의 실행을 멈추지 않고 다음 코드를 먼저 실행하는 자바스크립트의 특성

- 비동기 처리 예시

  - jquery ajax (서버에서 클라이언트 요청에 응답하는 방법 중 하나)

    ```javascript
    function getData() {
    	var tableData;
    	$.get('https://domain.com/products/1', function(response) {
    		tableData = response;
    	});
    	return tableData;
    }
    ```

  - setTimeout (web api의 한 종류)

    ```javascript
    // #1
    console.log('Hello');
    // #2
    setTimeout(function() {
    	console.log('Bye');
    }, 3000);
    // #3
    console.log('Hello Again');
    
    ```

     setTimeout() 역시 비동기 방식으로 실행되기 때문에 3초를 기다렸다가 다음 코드를 수행하는 것이 아니라 일단 setTimeout()을 실행하고 나서 바로 다음 코드인 `console.log('Hello Again');`으로 넘어갔습니다. 따라서, ‘Hello’, ‘Hello Again’를 먼저 출력하고 3초가 지나면 ‘Bye’가 출력됩니다. 

  - 파일읽기

    ```javascript
    const fs = require('fs')
    
    let content = ''
    
    console.log('파일읽기전')
    fs.readFile('me2.json', (err, data) => {
        setTimeout(() => {
            console.log(JSON.parse(data))
        }, 10000)
        // console.log('파일읽기')
    })
    
    console.log(content)
    // 비동기적 함수( , function)
    
    console.log('끝')
    ```

    결과는 '파일읽기전', '', '끝',  me2.json의 순서이다.

- 콜백 함수로 비동기 처리 방식의 문제점 해결

  - 콜백 함수는 데이터가 준비된 시점에서만 원하는 함수를 수행한다.

- 콜백지옥과 해결방법

  - promise나 async를 사용함

  - async예시

    - 파일읽기

      ```javascript
      const fs = require('fs')
      let content = ''
      console.log('파일 읽기전')
      content = fs.readFileSync('me2.json')
      console.log('읽기 종료')
      console.log(JSON.parse(content))
      console.log('끝')
      ```

      순서는 '파일읽기전', '읽기종료', 파일내용, '끝'

- 비동기 작업 처리 과정

  - 비동기 처리는 브라우저 조작 언어라는 특성으로인함.
  - 브라우저는 single thread 에서 이벤트기반(event driven) 방식으로 실행된다.
  - call stack : 함수가 호출되면 순차적으로 call stack 에 쌓이고 순차적으로 실행된다. task가 종료하기 전까지는 다른 task를 수행할 수 없다.
  - callback queu : 비동기처리 함수의 콜백, 타이머(setTimeout), 이벤트헨들러 등이 기록되는 곳으로 이벤트 루프에 의해 특정시점에 콜 스택으로 이동되어 실행 됨.
  - event loop : 콜 스택과 콜백 큐에 작업(실행될 함수)이 있는지 확인하며 작업을 실행한다.

###  1. [XMLHttpRequest](https://github.com/MinG822/WebApplication/blob/master/javascript/01_js_browser/02_giphy.html)

```javascript
//Giphy API 를 통해 data를 요청하고 가공하기
const searchAndPush = (keyword) => {
    const API_KEY = 'KEY'
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

    const GiphyAPICall = new XMLHttpRequest()
    GiphyAPICall.open('GET', URL)
    GiphyAPICall.send()

    // requests.get(url)
    GiphyAPICall.addEventListener('load', e => {
        const parsedData = JSON.parse(e.target.response)
        pushToDOM(parsedData)
    })
```



### 2. axios cdn

> axios는 브라우저에서 XHR(XMLHttpRequest)를 보내주고 그 결과를 promise 객체로 반환해주는 라이브러리이다. 비동기 처리가 완료되면 프로미스가 결과 값을 반환해주는 데, `then()`을 사용해 그 값을 받을 수 있다.

#### 1. 기본 활용법

```javascript
axios.get('/posts/')
	.then(function(response) {
    	console.log(response)
})

const data = {title: '제목', content: '내용'}
axios.post('/posts/', data)
	.then(function(response) {
    	console.log(response)
})
```

#### 2. [개념 확인하기](https://github.com/MinG822/WebApplication/blob/master/javascript/02_js_async/02_axios.js)

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script>
        const getDog = () => {
        axios.get('https://dog.ceo/api/breeds/image/random')
        .then(response => {
            console.log(response.data)
            console.log('데이터 도착했다!')
            })
        };
        console.log('함수 호출 시작한다!')
        getDog()
        console.log('함수 호출 끝났다!')
    </script>
```

- 해당 파일의 콘솔을 확인하면 `'함수 호출 시작한다!'`, `'함수 호출 끝났다!'`, `'데이터 도착했다!'`의 순으로 출력된다.

- 이는 파이썬(`blocking`) 과 자바스크립트(`non-blocking`)의 가장 큰 차이점이다. `axios` 는 `promise` 객체를 반환하여 `.then`을 통해 해당하는 작업(`axious` 요청작업)이 완료된(`resolve`) 경우 실행 될 로직을 구현할 수 있다. (`.catch` 에서는 `reject`된 결과를 받아서 처리할 수 있다.) - 콜백 지옥을 해결하기 위한 약속

---

## 4. Ajax 및 django

### 1. Ajax

> Ajax(Asynchronous JavaScript and XML, 에이잭스)는 비동기적인 웹 애플리케이션의 제작을 위해 아래와 같은 조합을 이용하는 웹 개발 기법이다.

- 조합
  - 표현 정보를 위한 HTML/CSS
  - 동적인 화면 출력 및 표시 정보와의 상호작용을 위한 DOM, JS
  - 웹 서버와 비동기적으로 데이터를 교환하고 조작하기 위한 데이터 - JSON(XML)
- Ajax 애플리케이션은 필요한 데이터만을 웹서버에 요청해서 받은 후 클라이언트에서 데이터에 대한 처리를 할 수 있다.
- 이것은 이미 존재하던 기술이었지만 2000년도 중반 이후로 인기를 끌기 시작했다. 구글은 2004년에 G메일, 2005년에 구글 지도 등의 웹 애플리케이션을 만들기 위해 비 동기식 통신을 사용했다.
- 웹 서버의 응답을 처리하기 위해 클라이언트 쪽에서는 자바스크립트를 쓴다. 웹 서버에서 전적으로 처리되던 데이터 처리의 일부분이 클라이언트 쪽에서 처리되므로 웹브라우저와 웹 서버 사이에 교환되는 데이터량과 웹서버의 데이터 처리량도 줄어들기 때문에 애플리케이션의 응답성이 좋아진다.
- 한편, 웹 개발자들은 때때로 Ajax를 단순히 웹페이지의 일부분을 대체하기 위해 사용한다. 비 AJAX 사용자가 전체 페이지를 불러오는 것에 비해 Ajax 사용자는 페이지의 일부분만을 불러올 수가 있다. 이것으로 개발자들이 비 AJAX환경에 있는 사용자의 접근성을 포함한 경험을 보호할 수 있으며, 적절한 브라우저를 이용하는 경우에 전체 페이지를 불러오는 일 없이 응답성을 향상시킬 수 있다.

### 2. [django 좋아요 기능 구현하기]( https://github.com/jarvis08/TIL/blob/master/04_Web/03_Javascript/05_Django_Like.md )

- detail.html

  ```html
  {% if user in article.like_users.all %}
        <button id="like-button" data-id="{{ article.pk }}" class="btn btn-outline-secondary">Unlike</button>
      {% else %}
        <button id="like-button" data-id="{{ article.pk }}" class="btn btn-danger">Like</button>
      {% endif %}
  
  <script>
    const likeButton = document.querySelector('#like-button')
    likeButton.addEventListener('click', function(e){
      const airticleId = e.target.dataset.id
      axios.get(`/articles/${airticleId}/like/`)
          .then(response => {
  ///////////////////////////////////////////////////////////
            document.querySelector('#like-count').innerText = response.data.count
  ///////////////////////////////////////////////////////////
            if (response.data.liked) {
              e.target.classList.remove('btn-danger')
              e.target.classList.add('btn-outline-secondary')
              e.target.innerText = 'Unlike'
            } else {
              e.target.classList.remove('btn-outline-secondary')
              e.target.classList.add('btn-danger')
              e.target.innerText = 'Like!'
            }
          })
    })
  </script>
  ```

- views.py

  ```python
  # views.py
  from django.http import Http404, HttpResponse, JsonResponse
  
  @login_required
  def like(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      user = request.user
      if article.like_users.filter(pk=user.pk).exists():
          article.like_users.remove(user)
          liked = False
      else:
          article.like_users.add(user)
          liked = True
  
      context = {
          'liked': liked,
          'count': article.like_users.count(),
      }
      return JsonResponse(context)
  ```

- 추가) axios + POST

  ```html
  <script>
      // 좋아요 버튼을 클릭하면, 좋아요 DB를 업데이트하고, 버튼을 바꾼다. (이벤트리스너)
      const likeButton = document.querySelector('#like-button')
      likeButton.addEventListener('click', function(e){
        // 좋아요 DB 업데이트 == 'articles/:id/like' 요청을 보냄
        const articleId = e.target.dataset.id
        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = 'X-CSRFToken'
        axios.post(`/articles/${articleId}/like/`)
            .then(response => {
              document.querySelector('#like-count').innerText = response.data.count
              if (response.data.liked) {
                e.target.classList.remove('btn-primary')
                e.target.classList.add('btn-outline-primary')
                e.target.innerText = '좋아요 취소'
              } else {
                e.target.classList.remove('btn-outline-primary')
                e.target.classList.add('btn-primary')
                e.target.innerText = '좋아요'
              }
            })
      })
    </script>
  ```