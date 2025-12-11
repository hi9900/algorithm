const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(input[0]);
let arr = input[1].split(' ').map(Number);

let arrow = new Array(1_000_001).fill(0);
let cnt = 0;

for (let i = 0; i < n; i++) {
  if (arrow[arr[i]] === 0) {
    arrow[arr[i] - 1] += 1;
    cnt += 1;
  } else {
    arrow[arr[i]] -= 1;
    arrow[arr[i] - 1] += 1;
  }
}

console.log(cnt);
