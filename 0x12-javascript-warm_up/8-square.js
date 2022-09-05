#!/usr/bin/node

const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < arg; x++) {
    let msg = '';
    for (let y = 0; y < arg; y++) {
      msg += 'X';
    }
    console.log(msg);
  }
}
