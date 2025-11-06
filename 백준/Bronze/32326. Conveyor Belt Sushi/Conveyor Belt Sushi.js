const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

const [r, g, b] = input.map(Number);

console.log(r * 3 + g * 4 + b * 5);