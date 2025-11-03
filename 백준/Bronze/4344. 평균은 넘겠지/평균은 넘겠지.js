const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const c = Number(input[0]);

for (let i = 1; i < c + 1; i++) {
  const [n, ...score] = input[i].split(' ').map(Number);

  // 평균
  const sumScore = score.reduce((acc, cur) => acc + cur, 0);
  const avg = sumScore / n;

  // 평균이 넘는 학생
  let students = 0;
  for (let j = 0; j < n; j++) {
    if (score[j] > avg) {
      students++;
    }
  }

  console.log(`${((students / n) * 100).toFixed(3)}%`);
}
