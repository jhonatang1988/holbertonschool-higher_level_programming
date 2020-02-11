#!/usr/bin/node
const Square = require('./5-square');
Square.prototype.charPrint = function (c) {
  if (c) {
    this.print(c);
  } else {
    this.print('X');
  }
};
module.exports = Square;
