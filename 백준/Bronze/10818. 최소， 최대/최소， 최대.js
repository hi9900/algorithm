const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]);
const arr = input[1].split(' ').map(Number);

let minNumber = 1_000_000;
let maxNumber = -1_000_000;

for (let i = 0; i < n; i++) {
  minNumber = Math.min(minNumber, arr[i]);
  maxNumber = Math.max(maxNumber, arr[i]);
}

console.log(minNumber, maxNumber);
