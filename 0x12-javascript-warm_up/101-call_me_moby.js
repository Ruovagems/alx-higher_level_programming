#!/usr/bin/node

const executeXTimes = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

// Example usage:
const myFunction = () => {
  console.log("Executing the function!");
};

executeXTimes(3, myFunction);
