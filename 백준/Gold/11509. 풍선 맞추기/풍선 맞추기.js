const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(input[0]);
let arr = input[1].split(' ').map(Number);

let arrow = new Array(1_000_001).fill(0);
let cnt = 0;

for (let x of arr) {
  if (arrow[x] === 0) {
    arrow[x - 1] += 1;
    cnt += 1;
  } else {
    arrow[x] -= 1;
    arrow[x - 1] += 1;
  }
}

console.log(cnt);
