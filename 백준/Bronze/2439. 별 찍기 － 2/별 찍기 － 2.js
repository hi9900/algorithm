const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

const N = Number(input[0]);
let result = '';

for (let i = 1; i <= N; i++) {
  result += `${' '.repeat(N - i)}${'*'.repeat(i)}\n`;
}

console.log(result.trimEnd());