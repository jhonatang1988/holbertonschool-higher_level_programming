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

  rotate () {
    if (this.width && this.height) {
      this._temp = this.height;
      this.height = this.width;
      this.width = this._temp;
    }
  }

  double () {
    if (this.width && this.height) {
      this.width = this.width * 2;
      this.height = this.height * 2;
    }
  }
}
module.exports = Rectangle;
