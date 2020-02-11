#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const afile = require('child_process').execSync(`cat ${fileA} ${fileB}`).toString('UTF-8');
const fs = require('fs');
fs.writeFile(fileC, afile, function (err) {
  if (err) {
    return console.log(err);
  }
});
