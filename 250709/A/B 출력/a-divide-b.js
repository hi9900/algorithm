const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

let [a, b] = input.split(' ').map(Number)
let answer = `${parseInt(a / b)}.`

a %= b
for (let i=0; i<20; i++) {
    a *= 10
    answer += parseInt(a / b)
    a %= b
}

console.log(answer)