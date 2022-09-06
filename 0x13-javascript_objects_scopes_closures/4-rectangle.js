#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = this.height; x > 0; x--) {
      let msg = '';
      for (let y = this.width; y > 0; y--) {
        msg += 'X';
      }
      console.log(msg);
    }
  }

  rotate () {
    const swp = this.height;
    this.height = this.width;
    this.width = swp;
  }

  double () {
    (this.height) *= 2;
    (this.width) *= 2;
  }
}
module.exports = Rectangle;
