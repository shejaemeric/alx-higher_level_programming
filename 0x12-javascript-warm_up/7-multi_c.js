#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < arg; x++) {
    console.log('C is fun');
  }
}
