const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

const n = Number(input)

let i = 0
while (i < n) {
    console.log('*')
    i++
}