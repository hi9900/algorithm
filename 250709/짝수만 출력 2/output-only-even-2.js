const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

let [b, a] = input.split(' ').map(Number)
let answer = ''

while (b >= a) {
    answer += `${b} `
    b -= 2
}

console.log(answer.trim())