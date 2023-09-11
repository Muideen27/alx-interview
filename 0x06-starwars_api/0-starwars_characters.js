#!/usr/bin/node

const util = require('util');
const request = require('request');

if (process.argv[2] === undefined) {
  console.log('Usage: node <FILENAME> <id>');
} else {
  (async () => {
    const requestPromise = util.promisify(request);
    const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
    const body = (await requestPromise(url)).body;
    const abc = JSON.parse(body).characters;
    for (let i = 0; i < abc.length; i++) {
      const char = (await requestPromise(abc[i])).body;
      console.log(JSON.parse(char).name);
    }
  })();
}
