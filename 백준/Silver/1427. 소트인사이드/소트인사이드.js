const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = input[0].split('').map(Number);

n.sort((a, b) => b - a);
console.log(n.join(''));
