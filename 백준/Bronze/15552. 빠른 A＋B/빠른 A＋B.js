const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let T = Number(input[0]);
let result = '';

for (let i = 0; i < T; i++) {
  let [a, b] = input[i + 1].split(' ').map(Number);
  result += a + b + '\n';
}

console.log(result);
