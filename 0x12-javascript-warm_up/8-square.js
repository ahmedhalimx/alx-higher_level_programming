#!/usr/bin/node
const argv = process.argv;

if (!isNaN(argv[2])) {
  for (let i = 0; i < argv[2]; i++) {
    let block = '';
    for (let j = 0; j < argv[2]; j++) {
      block += 'X';
    }
    console.log(block);
  }
} else {
  console.log('Missing size');
}
