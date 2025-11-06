const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

const n = Number(input[0]);

let result = '';
for (let i = n; i > 0; i--) {
  result += `${i}\n`;
}

console.log(result.trimEnd());