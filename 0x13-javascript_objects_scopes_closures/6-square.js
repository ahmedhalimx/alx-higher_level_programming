#!/usr/bin/node

const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let h = 0; h < this.width; ++h) {
      let block = '';
      for (let w = 0; w < this.width; ++w) { block += c; }
      console.log(block);
    }
  }
}

module.exports = Square;
