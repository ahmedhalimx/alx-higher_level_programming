#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  return (+a + +b);
}

if (isNaN(argv[2]) || isNaN(argv[3])) {
  console.log('NaN');
} else {
  console.log(add(argv[2], argv[3]));
}
