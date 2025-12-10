const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(input[0]);
let five = Math.floor(n / 5);
let answer = 5001;

for (let i = five; i >= 0; i--) {
  let x = n - 5 * i;
  if (x % 3 === 0) {
    answer = Math.min(answer, i + Math.floor(x / 3));
  }
}

if (answer === 5001) console.log(-1);
else console.log(answer);
