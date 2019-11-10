function add(x, y) {
    return x + y
}

// function expression 함수 표현식 (주로 사용)
const sub = function(x, y) {
    return x - y
}

// arrow function (ES6)
const mul = (x, y) => {
    return x * y
}

const ssafy = function (name) {
    return `안녕, ${name}`
}

// 인자쪽 괄호는 인자가 1개만 있을 때,
// 블락을 없애는 조건은 표현식이 하나만 있을 경우
// const ssafy = name => `안녕, ${name}`
// const ssafy1 = () => {}

// const square = function (num) {
//     return num ** 2
// }

const square = num => num ** 2

console.log(square(2))

const sayHello = () => 'hello'
console.log(sayHello())

const sayHello2 = (name='anonymous') => `hello ${name}`

console.log(sayHello2())