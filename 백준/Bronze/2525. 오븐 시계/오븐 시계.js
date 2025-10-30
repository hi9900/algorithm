const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let [a, b] = input[0].split(' ').map(Number);
let c = Number(input[1]);

if (b + c >= 60) {
  a += parseInt((b + c) / 60);
  b = (b + c) % 60;
} else {
  b += c;
}

if (a >= 24) {
  a -= 24;
}

console.log(a, b);
