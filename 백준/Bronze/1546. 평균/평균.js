const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]);
const score = input[1].split(' ').map(Number);

let maxScore = score.reduce((acc, cur) => Math.max(acc, cur));

let sumNewScore = 0;
for (let i = 0; i < n; i++) {
  sumNewScore += (score[i] / maxScore) * 100;
}
console.log(sumNewScore / n);
