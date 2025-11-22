#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;

    function printCharacter (index) {
      if (index >= characters.length) return;
      request.get(characters[index], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
          printCharacter(index + 1);
        }
      });
    }

    printCharacter(0);
  }
});
