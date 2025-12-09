const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let [n, k] = input[0].split(' ').map(Number);
let coins = [];

for (let i = 1; i <= n; i++) {
  coins.push(Number(input[i]));
}
coins.reverse();

let answer = 0;
for (const coin of coins) {
  answer += Math.floor(k / coin);
  k %= coin;
}

console.log(answer);
