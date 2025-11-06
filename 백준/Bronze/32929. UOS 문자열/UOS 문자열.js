const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

const x = Number(input[0]);

console.log('UOSUOS'[x % 3 + 2]);