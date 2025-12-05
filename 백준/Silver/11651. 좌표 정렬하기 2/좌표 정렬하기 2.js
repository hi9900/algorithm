const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

function compare(a, b) {
  if (a[1] === b[1]) {
    return a[0] - b[0];
  }

  return a[1] - b[1];
}

let n = Number(input[0]);
let arr = new Array(n).fill([0, 0]);

for (let i = 1; i <= n; i++) {
  let [x, y] = input[i].split(' ').map(Number);
  arr[i - 1] = [x, y];
}

arr.sort(compare);

let answer = '';
for (let i = 0; i < n; i++) {
  answer += `${arr[i][0]} ${arr[i][1]}\n`;
}

console.log(answer.trimEnd());
