#!/usr/bin/node
exports.addMeMaybe = function (number, theFunc) {
  number++;
  theFunc(number);
};
