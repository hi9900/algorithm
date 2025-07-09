const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

let [a, b] = input.split(' ').map(Number)
let answer = ''

if (a > b) {
    for (let i=a; i>=b; i--) {
        answer += `${i} `
    }
} else {
    for (let i=b; i>=a; i--) {
        answer += `${i} `
    }
}

console.log(answer.trim())