const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

let [a, n] = input.split(' ').map(Number)

for (let i=0; i<n; i++) {
    a += n
    console.log(a)
}