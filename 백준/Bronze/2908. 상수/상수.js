const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [a, b] = input[0].split(' ');

let revA = a.split('').reduce((acc, cur) => cur + acc, '');
let revB = b.split('').reduce((acc, cur) => cur + acc, '');

revA = Number(revA);
revB = Number(revB);
console.log(Math.max(revA, revB));
