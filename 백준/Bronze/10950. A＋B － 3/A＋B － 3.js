const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().split('\n');

let t = Number(input[0]);

let answer = '';

for (let i = 1; i <= t; i++) {
  let [a, b] = input[i].split(' ').map(Number);

  answer += `${a + b}\n`;
}

console.log(answer.trimEnd());
