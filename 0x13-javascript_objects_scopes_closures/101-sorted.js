#!/usr/bin/node
const initdict = require('./101-data').dict;

const newObj = {};
const unique = new Set(Object.values(initdict));
unique.forEach(num => {
  newObj[num] = [];
});

for (const [keyn, valuen] of Object.entries(newObj)) {
  for (const [keyi, valuei] of Object.entries(initdict)) {
    if (keyn.toString() === valuei.toString()) {
      valuen.push(keyi);
      newObj[keyn] = valuen;
    }
  }
}
console.log(newObj);
