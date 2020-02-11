#!/usr/bin/node
const initlist = require('./100-data').list;

const finlist = initlist.map(function (num, index) {
  return num * index;
});

console.log(initlist);
console.log(finlist);
