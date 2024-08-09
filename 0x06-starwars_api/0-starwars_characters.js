#!/usr/bin/node

const request = require('request');
// const JSON = require('JSON')

const url = 'https://swapi-api.alx-tools.com/api/people';
request(url, (error, respoinse, body) => {
  console.log(typeof body);
//	characters = JSON.parse(body.results)
//	console.log(type(characters))
//	for (const person of characters) {
//		console.log(person.name)
//	}
}
);
