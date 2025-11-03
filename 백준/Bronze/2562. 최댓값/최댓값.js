const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const arr = input.map(Number);
let maxNumber = 0;
let maxIndex = 0;

for (let i = 0; i < 9; i++) {
  if (arr[i] > maxNumber) {
    maxNumber = arr[i];
    maxIndex = i + 1;
  }
}

console.log(maxNumber);
console.log(maxIndex);
