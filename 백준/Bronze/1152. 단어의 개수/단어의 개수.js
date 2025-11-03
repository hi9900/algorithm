const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const strings = input[0].trim().split(' ');

if (strings.length === 1 && strings[0] == '') console.log(0);
else console.log(strings.length);
