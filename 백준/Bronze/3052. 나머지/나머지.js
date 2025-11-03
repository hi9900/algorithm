const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const arr = input.map(Number);
let mySet = new Set();
for (let i = 0; i < 10; i++) {
  mySet.add(arr[i] % 42);
}

console.log(mySet.size);
