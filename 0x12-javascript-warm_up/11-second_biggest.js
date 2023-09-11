#!/usr/bin/node
const argv = process.argv;

function second (Array) {
  if (Array.length === 2 || Array.length === 3) {
    return (0);
  }

  let max = Array[2];
  let preMax = Array[3];

  for (let i = 2; i < Array.length; i++) {
    if (Array[i] > max) {
      preMax = max;
      max = Array[i];
    } else if (Array[i] > preMax && Array[i] < max) {
      preMax = Array[i];
    }
  }
  return (preMax);
}

console.log(second(argv));
