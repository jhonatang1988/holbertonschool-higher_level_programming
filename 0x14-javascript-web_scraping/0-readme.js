#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];

try {
  const data = fs.readFileSync(`./${fileA}`, 'utf8');
  console.log(data);
} catch (err) {
  console.log(err);
}
