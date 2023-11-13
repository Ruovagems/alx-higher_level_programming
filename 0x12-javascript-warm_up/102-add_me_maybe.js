#!/usr/bin/node

const incrementAndCall = (number, theFunction) => {
  const incrementedNumber = number + 1;
  theFunction(incrementedNumber);
};

// Example usage:
const myFunction = (value) => {
  console.log(`Value received: ${value}`);
};

incrementAndCall(5, myFunction);
