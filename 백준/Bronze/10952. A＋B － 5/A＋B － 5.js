const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().split('\n');

let i = 0;
let answer = '';

while (1) {
  let [a, b] = input[i].split(' ').map(Number);

  if (a === 0 && b === 0) break;
  answer += `${a + b}\n`;
  i++;
}

console.log(answer.trimEnd());
