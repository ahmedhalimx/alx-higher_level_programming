#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = 0; h < this.height; ++h) {
      let rowWidth = '';
      for (let w = 0; w < this.width; ++w) {
        rowWidth += 'X';
      }
      console.log(rowWidth);
    }
  }
}

module.exports = Rectangle;
