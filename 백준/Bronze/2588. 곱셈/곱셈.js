const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let [a, b] = input.map(Number);

let result = 0;
for (let i = 0; i < 3; i++) {
  let ans = a * (b % 10);
  result += ans * 10 ** i;
  console.log(ans);
  b = parseInt(b / 10);
}

console.log(result);
