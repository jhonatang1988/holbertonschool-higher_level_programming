#!/usr/bin/node
const SquareSuper = require('./5-square');
class Square extends SquareSuper {
    constructor(size){
	super(size, size);
    }
    charPrint(c){
	if(c) {
	    this.print(c);
	} else {
	    this.print('X');
	}
    }
};
module.exports = Square;
