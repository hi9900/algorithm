const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

function compare(a, b) {
  return a.length - b.length;
}

let n = Number(input[0]);
let strSet = new Set();

for (let i = 1; i <= n; i++) {
  strSet.add(input[i]);
}

let arr = [...strSet];
arr.sort();
arr.sort(compare);
console.log(arr.join('\n'));
