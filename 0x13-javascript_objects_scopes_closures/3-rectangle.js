#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    const th = this;
    if (Number.isInteger(w) && w > 0) {
      if (Number.isInteger(h) && h > 0) {
        th.width = w;
        th.height = h;
      }
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('X');
        }
        console.log();
      }
    }
  }
}
module.exports = Rectangle;
