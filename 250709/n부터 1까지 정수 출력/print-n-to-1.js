const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

let n = Number(input)
let answer = ''
while (n > 0) {
    answer += `${n} `
    n--
}

console.log(answer)