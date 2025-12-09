const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]);
const arr = input[1].split(' ').map(Number);
arr.sort((a, b) => a - b);

let answer = 0;
for (let i = 0; i < n; i++) {
  const wait = arr.slice(0, i).reduce((a, c) => a + c, 0);
  answer += wait + arr[i];
}

console.log(answer);
