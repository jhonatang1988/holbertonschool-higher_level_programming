#!/usr/bin/node
const SquareSuper = require('./5-square');
class Square extends SquareSuper {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          if (c) {
            process.stdout.write(c);
          } else {
            process.stdout.write('X');
          }
        }
        console.log();
      }
    }
  }
}
module.exports = Square;
