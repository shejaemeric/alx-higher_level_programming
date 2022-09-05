#!/usr/bin/node
exports.callMeMoby = function (x, theFunc) {
  for (let y = 0; y < x; y++) {
    theFunc();
  }
};
