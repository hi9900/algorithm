const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]);
const numbers = input[1].split('').map(Number);

let sumNumbers = numbers.reduce((acc, cur) => acc + cur, 0);
console.log(sumNumbers);
