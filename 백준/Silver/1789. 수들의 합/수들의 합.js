const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let s = Number(input[0]);

let sumNums = 0;
let i = 0;

while (sumNums <= s) {
  i++;
  sumNums += i;
}

console.log(i - 1);
