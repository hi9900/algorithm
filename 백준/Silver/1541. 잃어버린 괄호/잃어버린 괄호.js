const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let values = input[0].split('-');
let answer = 0;

for (let i = 0; i < values.length; i++) {
  const calcSum = values[i]
    .split('+')
    .map(Number)
    .reduce((a, c) => a + c, 0);

  if (i === 0) {
    answer += calcSum;
  } else {
    answer -= calcSum;
  }
}

console.log(answer);
