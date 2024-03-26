#!/usr/bin/node

const statuscode = require('request');

statuscode(process.argv[2], function (_err, code) {
  console.log('code:', code.statusCode);
});
