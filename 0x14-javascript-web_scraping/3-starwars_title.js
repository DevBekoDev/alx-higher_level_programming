#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(url, function (err, result, body) {
    body = JSON.parse(body);
    console.log(body.title);
});
