#!/usr/bin/node
const dict = require('./101-data');

const userOccurrenceDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (!(occurrence in userOccurrenceDict)) {
    userOccurrenceDict[occurrence] = [];
  }
  userOccurrenceDict[occurrence].push(userId);
}

console.log(userOccurrenceDict);
