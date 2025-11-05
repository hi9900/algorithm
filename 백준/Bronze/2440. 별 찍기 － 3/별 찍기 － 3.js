const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

const N = Number(input[0]);
let result = '';

for (let i = N; i > 0; i--) {
  result += `${'*'.repeat(i)}\n`;
}

console.log(result.trimEnd());