#!/usr/bin/node
const argv = process.argv;

function second (array) {
  if (array.length === 2 || array.length === 3) {
	  return (0);
  }

  let max = array[2];
  let previously_max = array[3];

  for (let i = 2; i < array.length; i++) {
    if (array[i] > max) {
      previously_max = max;
      max = array[i];
    } else if (array[i] > previously_max && array[i] < max) {
      previously_max = array[i];
    }
  }

  return (previously_max);
}

console.log(second(argv));
