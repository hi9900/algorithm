const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().split('\n');

let n = Number(input[0]);
let answer = 1;
for (let i = 1; i <= n; i++) {
  answer *= i;
}
console.log(answer);
