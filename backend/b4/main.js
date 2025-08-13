// const myInfo = {
//     name: 'Alice',
//     age: 20
// }

// for (const key in myInfo) {
//     console.log(key)
// }

// function hello(name) {
//     return "Xin chao, " + name
// }

// console.log(hello("Minh"))

// ES6
// const tong = (a, b) => a + b

// console.log(tong(1, 2))

// const fruits = ["Apple", "Banana", "Orange"];

// console.log(fruits[0])
// console.log(fruits.length)

// fruits.push("Grape")
// console.log(fruits)

// fruits.pop()
// console.log(fruits)

// fruits.unshift("Kiwi")
// console.log(fruits)

// fruits.shift()
// console.log(fruits)

// fruits.forEach((fruit, index,) => {
//     console.log(`${index} ${fruit}`)
// })


const numbers = [1, 2, 3, 4]

console.log(numbers.map((i) => i ** 2))
console.log(numbers.reduce((x, y) => x + y))
console.log(numbers)


/**
 * Scope - Pham vi
 * Global scope: biến có truy cập từ bất cứ đâu
 * Function scope: biến chỉ được sử dụng bên trong hàm
 * Block scope: Biến có có pham vi nằm bên trong block {}
 */

var globalVar = 'Đây là biến toàn cục'

function exampleScope() {
    var functionVar = 'Phạm vi biến của hàm';
    let blockVar = 'Phạm vi khối'; // Phạm vi khối
    const constBlockVar = 'Phạm vi khối'

    if (true) {
        let insideVar = 'Phạm vi bên trong if'
        console.log(blockVar)
        {
            console.log(blockVar)
            {
                console.log(blockVar)
            }
        }
    }
    console.log(insideVar)


}