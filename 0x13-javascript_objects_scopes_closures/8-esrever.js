#!/usr/bin/node
exports.esrever = function (list) {
  const reverselist = [];
  for (const i in list) {
    reverselist.push(list.slice(-i - 1)[0]);
  }
  return reverselist;
};
