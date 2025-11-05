const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

const N = Number(input[0]);
let result = '';

for (let i = 1; i < 2 * N; i++) {
  if (i > N) {
    result += `${' '.repeat(i - N)}${'*'.repeat(2 * (2 * N - i) - 1)}\n`;
  } else {
    result += `${' '.repeat(N - i)}${'*'.repeat(2 * i - 1)}\n`;
  }
}

console.log(result.trimEnd());