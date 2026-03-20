#!/usr/bin/node
const { argv } = require('node:process');
const first = argv[2];
const second = argv[3];

console.log(`${first} is ${second}`);
