const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(input[0]);
let arr = new Array(n).fill(0);

for (let i = 1; i <= n; i++) {
  arr[i - 1] = Number(input[i]);
}

arr.sort((a, b) => a - b);
console.log(arr.join('\n'));
