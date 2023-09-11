#!/usr/bin/node
let argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  argv = argv.map(Number)
    .slice(2, argv.length)
    .sort((a, b) => a - b);
  console.log(argv[argv.length - 2]);
}
