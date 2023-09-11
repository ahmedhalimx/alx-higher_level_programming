#!/usr/bin/node
const argv = process.argv;

if (!isNaN(parseInt(argv[2]))) {
  const counter = parseInt(argv[2]);
  for (let i = 0; i < counter; ++i) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
