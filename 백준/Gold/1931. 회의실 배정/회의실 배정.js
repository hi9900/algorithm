const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(input[0]);
let arr = [];

for (let i = 1; i <= n; i++) {
  let time = input[i].split(' ').map(Number);
  arr.push(time);
}

arr.sort((x, y) => {
  if (x[1] === y[1]) return x[0] - y[0]; // 같으면, 시작 시점
  // 종료 시점 기준 정렬
  return x[1] - y[1];
});

let cnt = 0;
let lastTime = 0;

for ([s, e] of arr) {
  if (lastTime <= s) {
    lastTime = e;
    cnt += 1;
  }
}

console.log(cnt);
