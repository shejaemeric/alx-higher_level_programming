#!/usr/bin/node
exports.esrever = function (list) {
  const listRev = [];
  let len = list.length - 1;
  if (list) {
    list.forEach(element => {
      listRev[len] = element;
      len--;
    });
  }
  return listRev;
};
