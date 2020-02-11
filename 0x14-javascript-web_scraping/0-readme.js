#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];

fs.readFile(`${fileA}`, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
