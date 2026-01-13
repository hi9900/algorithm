const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
console.log(Math.abs(n - m));
