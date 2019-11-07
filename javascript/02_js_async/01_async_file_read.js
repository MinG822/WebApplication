const fs = require('fs')

let content = ''

// console.log('파일읽기전')
// fs.readFile('me2.json', (err, data) => {
//     setTimeout(() => {
//         console.log(JSON.parse(data))
//     }, 10000)
//     // console.log('파일읽기')
// })

// console.log(content)
// 비동기적 함수( , function)

// console.log('끝')

console.log('파일 읽기전')

content = fs.readFileSync('me2.json')

console.log('읽기 종료')

console.log(JSON.parse(content))

console.log('끝')