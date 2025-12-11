const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(input[0]);
let road = input[1].split(' ').map(Number);
let price = input[2].split(' ').map(Number);
let minPrice = 1_000_000_001;
let result = 0;

for (let i = 0; i < n - 1; i++) {
  minPrice = Math.min(minPrice, price[i]);
  result += minPrice * road[i];
}

console.log(result);
