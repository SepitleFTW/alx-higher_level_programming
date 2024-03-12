#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let rect = 0; rect < this.height; rect++) {
      let s = '';
      for (let recta = 0; recta < this.width; recta++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}
module.exports = Rectangle;
