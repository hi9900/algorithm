const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

const N = Number(input[0]);
let result = '';

for (let i = 1; i < 2 * N; i += 2) {
  result += `${' '.repeat((2 * N - 1 - i) / 2)}${'*'.repeat(i)}\n`;
}

console.log(result.trimEnd());