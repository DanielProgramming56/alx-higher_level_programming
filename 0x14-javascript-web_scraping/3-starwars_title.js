#!/usr/bin/node
const request = require("request");
const id = process.argv[2];
const url = "https://swapi-api.alx-tools.com/api/films/" + id;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const jsonified = JSON.parse(body);
    console.log(jsonified.title);
  }
});
