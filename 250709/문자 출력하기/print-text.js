const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

const C = input
let answer = ''

for (let i=0; i<8; i++) {
    answer += C
}

console.log(answer)