const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let [a, b, c] = input[0].split(' ').map(Number);

if (a === b) {
  if (a === c) {
    console.log(10000 + a * 1000);
  } else {
    console.log(1000 + a * 100);
  }
} else if (b === c) {
  if (b === a) {
    console.log(10000 + b * 1000);
  } else {
    console.log(1000 + b * 100);
  }
} else if (a === c) {
  if (a === b) {
    console.log(10000 + a * 1000);
  } else {
    console.log(1000 + a * 100);
  }
} else {
  console.log(Math.max(a, b, c) * 100);
}
