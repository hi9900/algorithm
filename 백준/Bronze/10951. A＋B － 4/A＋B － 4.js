const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');

let n = input.length;
let answer = '';

for (let i = 0; i < n; i++) {
  let [a, b] = input[i].split(' ').map(Number);

  if (a === 0 && b === 0) break;
  answer += `${a + b}\n`;
}

console.log(answer.trimEnd());
