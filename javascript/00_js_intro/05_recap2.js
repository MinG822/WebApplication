let a = 1
let b = 2
console.log(a, b)
let c = a + b
console.log(c)
c = c + 10
console.log(c)
c -= 3
console.log(c)
c *= 10
console.log(c)
c++
console.log(c)
c--
console.log(c)

//Iteration(반복)
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

//Array(배열)
const numbers = [1, 2, 3, 4]

console.log(numbers[0])
console.log(numbers[-1])
console.log(numbers.length)

// 원본 파괴
numbers.reverse()
console.log(numbers)
numbers.reverse()
console.log(numbers)
numbers.push('a')
console.log(numbers)
numbers.pop()
console.log(numbers)
numbers.unshift('a')
console.log(numbers)
numbers.shift()
console.log(numbers)

console.log(numbers.includes(1))
console.log(numbers.includes(0))
numbers.push('a')
numbers.push('a')
console.log(numbers.indexOf('a'))
console.log(numbers.join())
console.log(numbers.join(''))
console.log(numbers.join('-'))

//Object(객체/오브젝트)
const me = {
    name: 'minG',
    'phone number': '01012345678',
    appleProducts: {
        ipad: '2018pro',
        iphone: '6s+',
        macbook: '2018 pro'
    }
}

console.log(me.name)
console.log(me['name'])
console.log(me['phone number'])
console.log(me['phone number1'])
console.log(me.name1)
console.log(typeof me['phone number'])
console.log(me.appleProducts)
console.log(typeof me.appleProducts)
console.log(me.appleProducts.ipad)

//Object => JSON

const jsonData = JSON.stringify({
    coffee: 'Americano',
    iceCream: {k: 23},
})

console.log(jsonData)
console.log(typeof jsonData)

//Json => Object
const parseData = JSON.parse(jsonData)
console.log(parseData)
console.log(typeof parseData)

//Array Helper Methods(배열 헬퍼 메서드)
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
// node의 전역객체는 global
// Object.keys(global)
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

console.log(findWhere(ladders, {height:20}))

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

// Function
// function 키워드를 통한 정의
function add(num1, num2) {
    return num1 + num2
}

console.log(add(1, 2))

const sub = function(num1, num2) {
    return num1 - num2
}

console.log(sub(10, 5))
console.log(typeof add, typeof sub)

// arrow function 을 통한 정의
const mul = (num1, num2) => {
    return num1*num2
}

// arrow function refactory
// 일반적으로 함수는 const로 바인딩하지만,
// 콘솔에서 리팩토링할 때 함수 재할당에러가 날 수 있으니 let으로 선언하는 경우
// 리팩토링??, 함수 고치는거?
let square = num => {num**2}

let noArgs = () => 'No args'
noArgs = _ => 'No args'

let returnObject = () => { return { key: 'value'}}
// 괄호를 안하면 함수블록으로 인식!
returnObject = () => ({ket:'value'})
console.log(returnObject())

//기본인자를 줄 때는 인자 갯수와 상관없이 꼭 괄호를 해야한다.
// Anonymous function (익명/1회용 함수)

console.log((function (num) { return num**3})(2))
console.log((num => num**0.5)(4))

// function(){}와 ()=> {}는 문법만 다르고 완전히 똑같이 동작하는 것 처럼 보이지만
// this 키워드가 등장하게 되면, 둘은 다르게 동작한다. 


// 파이썬 친화적인 문법으로 진입장벽을 높이지 않기 위해서 lodash 모듈을 node환경에서 불러와 사용하기
// lodash 는 파이썬 문법을 포함한 여러 편리한 메서드를 제공하는 모듈

// 메뉴 고르기 (Array)
const _ = require('lodash')
const list = ['짜장면', '짬뽕', '볶음밥']
const pick = _.sample(list)
console.log(`오늘의 메뉴는 ${pick}입니다.`)

// 사진과 함께 메뉴고르기 (Object)

const object = {
    짜장면: 'http://recipe1.ezmember.co.kr/cache/recipe/2016/07/02/40c4f639ca973d9acccecdf7cbe0cbc41.jpg',
    짬뽕: 'http://recipe1.ezmember.co.kr/cache/recipe/2015/08/24/835a29917b3a9f074cb8d1636adeefcf1.jpg',
    볶음밥: 'http://recipe1.ezmember.co.kr/cache/recipe/2015/08/27/932b0eac49b0f341ee9b91553d84d9b91.jpg',
}

console.log(object[pick])

// 로또 번호 뽑기 (Python Syntax)
const numbers4 = _.range(1, 46)
const pick2 = _.sampleSize(numbers4, 6)
console.log(pick2)
console.log(`행운의 번호: ${pick2}`)

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

