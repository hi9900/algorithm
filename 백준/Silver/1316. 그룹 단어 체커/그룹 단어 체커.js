const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]);
let result = n;

for (let i = 1; i < n + 1; i++) {
  const word = input[i];

  for (let j = 0; j < word.length; j++) {
    if (word.slice(j + 1).includes(word[j]) && word[j + 1] !== word[j]) {
      result -= 1;
      break;
    }
  }
}

console.log(result);
