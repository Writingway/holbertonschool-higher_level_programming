#!/usr/bin/node
module.exports.add = function (a, b) {
  return a + b;
};

const add = require('./13-add').add;
console.log(add(3, 5));
