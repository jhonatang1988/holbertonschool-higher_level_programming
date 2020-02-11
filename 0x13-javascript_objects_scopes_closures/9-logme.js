#!/usr/bin/node
let counter = 0;
exports.logMe = function (item) {
  const num = counterplus();
  console.log(`${num}: ${item}`);
};
function counterplus () {
  return counter++;
}
