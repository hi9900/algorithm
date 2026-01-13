const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().split('\n');

let year = Number(input[0]);

if (year % 4 === 0 && (year % 100 || year % 400 === 0)) {
  console.log(1);
} else {
  console.log(0);
}
