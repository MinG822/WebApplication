const nothing = () => {
    console.log('3초 끝남')
}

const nothing2 = () => {
    console.log('10초 끝남')
}

console.log('start')

setTimeout(nothing2, 2000)

setTimeout(nothing, 3000)

console.log('end')