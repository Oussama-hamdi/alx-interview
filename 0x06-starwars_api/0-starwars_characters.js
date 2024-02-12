#!/usr/bin/node
/* Prints all characters of a Star Wars movie */

const request = require("request");
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, async (err, req, body) => {
  if (err) console.log(err);

  const movieData = await JSON.parse(body).characters;

  for (const characterUrl of movieData) {
    const characterResponse = await new Promise((resolve, reject) => {
      request(characterUrl, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(body);
        }
      });
    });

    const characterData = JSON.parse(characterResponse);
    console.log(characterData.name);
  }
});
