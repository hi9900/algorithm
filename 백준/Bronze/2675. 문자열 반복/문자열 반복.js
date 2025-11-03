const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const t = Number(input[0]);

for (let i = 1; i < t + 1; i++) {
  let [r, s] = input[i].split(' ');
  r = Number(r);
  
  let result = '';
  for (let j = 0; j < s.length; j++) {
    result += s[j].repeat(r);
  }

  console.log(result);
}
