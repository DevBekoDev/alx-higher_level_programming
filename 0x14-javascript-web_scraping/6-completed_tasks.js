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
      const completed = body[i].completed;

      if (completed && !doneByUser[userId]) {
        doneByUser[userId] = 0;
      }

      if (completed) ++doneByUser[userId];
    }
    console.log(doneByUser);
  }
});
