#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2);
  const sorted = list.sort();
  console.log(sorted[sorted.length - 2]);
}
