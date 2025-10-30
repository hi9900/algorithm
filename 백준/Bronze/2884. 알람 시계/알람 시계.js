const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');

let [h, m] = input.map(Number);

if (m - 45 < 0) {
  h -= 1;
  if (h < 0) {
    h += 24;
  }
  m = 60 + (m - 45);
} else {
  m -= 45;
}

console.log(h, m);
