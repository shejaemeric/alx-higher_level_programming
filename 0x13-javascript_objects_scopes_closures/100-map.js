#!/usr/bin/node
const ogList = require('./100-data').list;
let count = 0;
const newList = ogList.map((Element) => {
  return Element * (count++);
});
console.log(ogList);
console.log(newList);
