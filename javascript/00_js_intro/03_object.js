const fs = require('fs')

const me = {
    name: 'john',
    // sleep: function() {
    //     console.log('쿨쿨')
    // },
    appleProducts: {
        macBook: '2018pro',
        iPad: '2018pro',
    },
}

console.log(me['name'])
// console.log(me[name]) (X)

console.log(me.name)

// console.log(me.sleep())

console.log(me.appleProducts.macBook)

// JSON(JavaScript Object Notation)


const meJSON = JSON.stringify(me)
// object -> JSON(string)
console.log(typeof meJSON)

fs.writeFile('me.json', meJSON, err => {})

fs.writeFileSync('me2.json', meJSON)

// JSON.parse() 
// JSON(string) -> object
const meObject = JSON.parse(meJSON)
console.log(meObject)
console.log(meJSON)