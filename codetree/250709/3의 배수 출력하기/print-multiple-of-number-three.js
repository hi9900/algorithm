const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

const n = Number(input)

let i = 3
let answer = ''

while (i <= n) {
    answer += `${i} `
    i += 3
}

console.log(answer)