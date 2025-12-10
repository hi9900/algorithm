const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let [a, b] = input[0].split(' ').map(Number);

let answer = 10e9;
let flag = false;

function sol(a, b, t) {
  if (a === b) {
    flag = true;
    answer = Math.min(answer, t);
    return;
  }

  if (flag || a > b) return;

  sol(a * 2, b, t + 1);
  sol(Number(`${a}1`), b, t + 1);
}

sol(a, b, 1);

if (!flag) console.log(-1);
else console.log(answer);
