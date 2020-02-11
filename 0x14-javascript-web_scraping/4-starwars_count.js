#!/usr/bin/node
const r = require('request');
const url = process.argv[2];
let page;
r(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    page = '1';
    while (page) {
      const jsonbody = JSON.parse(body);
      page = jsonbody.next;
      console.log(parseInt(jsonbody.results.map(function (film, index) {
        return film.characters.filter(function (character, index) {
          return character === 'https://swapi.co/api/people/18/';
        });
      }).filter(function (movie) {
        return movie.length > 0;
      }).length));
    }
  }
});
