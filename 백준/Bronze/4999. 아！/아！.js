const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

const say = input[0];
const want = input[1];

console.log(say.includes(want) ? 'go' : 'no');