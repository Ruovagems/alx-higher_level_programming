#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(apiUrl, function (error, response, body) {
  try {
    if (!error && response.statusCode === 200) {
      const json = JSON.parse(body);
      if (json.title) {
        console.log(json.title);
      } else {
        console.error('Title not found in the API response.');
      }
    } else {
      console.error('Error:', error);
    }
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
