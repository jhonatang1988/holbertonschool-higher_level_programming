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
}
module.exports = Rectangle;
