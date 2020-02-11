#!/usr/bin/node
const r = require('request');
const url = `${process.argv[2]}/?format=json`;
let page;
r(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      page = '1';
      while (page) {
        const jsonbody = JSON.parse(body);
        page = jsonbody.next;
        console.log(jsonbody.results.map(function (film, index) {
          return film.characters.filter(function (character, index) {
            return character === 'https://swapi.co/api/people/18/';
          });
        }).filter(function (movie) {
          return movie.length > 0;
        }).length);
      }
    } else {
      console.log('api caida');
    }
  }
});
