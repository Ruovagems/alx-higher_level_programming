#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: concatFiles.js <file1> <file2> <destination>');
  process.exit(1);
}

const [,, file1, file2, destination] = process.argv;

const data1 = fs.readFileSync(file1, 'utf8');
const data2 = fs.readFileSync(file2, 'utf8');
const concatenatedData = data1 + data2;

fs.writeFileSync(destination, concatenatedData);
