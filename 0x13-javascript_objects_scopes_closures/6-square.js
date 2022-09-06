#!/usr/bin/node
const Square_ = require('./5-square');
class Square extends Square_ {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      let msg = '';
      for (let x = this.height; x > 0; x--) {
        for (let y = this.height; y > 0; y--) {
          msg += c;
        }
        console.log(msg);
        msg = '';
      }
    }
  }
}
module.exports = Square;
