#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, _result, body) {
  if (err) {
    console.log(err);
  } else {
    const doneByUser = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      // Extract the userId and completed properties from each element
      const userId = body[i].userId;
      const done = body[i].done;

      if (done && !doneByUser[userId]) {
        doneByUser[userId] = 0;
      }

      if (done) ++doneByUser[userId];
    }
    console.log(doneByUser);
  }
});
