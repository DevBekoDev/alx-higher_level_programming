#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv.length === 2) {
  console.log(1);
} else {
  function factorial (a) {
    if (a === 0 || a === 1) {
      return 1;
    } else {
      return a * factorial(a - 1);
    }
  }
  console.log(factorial(parseInt(process.argv[2])));
}
