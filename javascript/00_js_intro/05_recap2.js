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
    iceCream: 'Cookie and cream',
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
    {id: 1, heights: 20},
    {id: 3, heights: 25},
]

function findWhere(array, criteria) {
    const property = Object.keys(criteria)[0]
    // criteria라는 오브젝트의 키값이 배열로 나오는데 첫번째값을 property에 저장한다.
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
    return array.find(temp => {
        return temp[property] === criteria[property]
    })
}

console.log(findWhere(ladders, { height: 20 }))