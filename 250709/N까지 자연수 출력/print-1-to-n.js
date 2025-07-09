const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

const N = Number(input)
let i = 1
let answer = ''

while (i <= N) {
    answer += `${i} `
    i++
}

console.log(answer)