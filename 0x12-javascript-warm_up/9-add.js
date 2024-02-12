#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  return result;
}

console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
