const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

let [c, n] = input.split(' ')
n = Number(n)
let answer = ''

if (c === 'A') {
    for (let i=1; i<=n; i++) {
        answer += `${i} `
    }
} else if (c === 'D') {
    for (let i=n; i>0; i--) {
        answer += `${i} `
    }
}

console.log(answer.trim())