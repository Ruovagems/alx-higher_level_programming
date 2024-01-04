#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  try {
    if (!error && response.statusCode === 200) {
      const film = JSON.parse(body);
      const charactersUrls = film.characters;

      const fetchCharacterName = (url) => {
        return new Promise((resolve, reject) => {
          request(url, (err, res, b) => {
            if (!err && res.statusCode === 200) {
              const character = JSON.parse(b);
              resolve(character.name);
            } else {
              reject(err);
            }
          });
        });
      };

      // Fetch character names in order
      charactersUrls.reduce((sequence, url) => {
        return sequence.then(() => {
          return fetchCharacterName(url).then((name) => {
            console.log(name);
          });
        });
      }, Promise.resolve());
    } else {
      console.error('Error:', error);
    }
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
