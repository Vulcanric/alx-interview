#!/usr/bin/node
/**
 * Retreives data from an api and print it out to the console
 *
 * API:
 * ----
 *   https://swapi-api.alx-tools.com/api
 * Description:
 * ------------
 *   The swapi api is the world's first quantified and programmati-
 * cally-accessible data source for all data from the Star Wars canon universe
 *
 * Goal:
 * -----
 *   Retrieve all characters of a film given the film id as cmdline argument
 */
const request = require('request');

let API = 'https://swapi-api.alx-tools.com/api/';

// Get film ID
const filmID = process.argv[2];
API += `films/${filmID}`;

request(API, (error, response, body) => {
  try {
    // Convert JSON string to JS Objects
    if (error) {
      console.error(error);
    } else {
      const film = JSON.parse(body);
      const characters = film.characters;
      // console.log(film)
      for (const actorURL of characters) {
        request(actorURL, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            const actor = JSON.parse(body);
            console.log(actor.name);
          }
        });
      }
    }
  } catch (err) {
    // console.error(err.message);
  }
});
