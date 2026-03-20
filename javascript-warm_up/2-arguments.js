#!/usr/bin/node
const { argv } = require('node:process');

// print process.argv
if (!argv[2]) {
    console.log('No argument')
} else {
    console.log('Argument found');
}
