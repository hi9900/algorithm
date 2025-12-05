const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(input[0]);

let arrX = input[1].split(' ').map(Number);
let setX = new Set(arrX);
let sortedX = [...setX].sort((a, b) => a - b);
let dictX = {};

sortedX.forEach((v, i) => {
  dictX[v] = i;
});

let answer = '';
for (let i = 0; i < n; i++) {
  answer += `${dictX[arrX[i]]} `;
}

console.log(answer.trimEnd());
