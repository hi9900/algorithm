const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

let [a, b] = input.split(' ').map(Number)
let answer = ''

if (a > 0) {
    for (let i=0; i<b; i++) {
        answer += a
    }
    console.log(answer)
} else {
    console.log(0)
}
