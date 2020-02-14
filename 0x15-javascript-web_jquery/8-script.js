function DocumentReady () {
  $.getJSON('https://swapi.co/api/films/?format=json',
    function (data) {
      console.log(data);
      $.each(data.results, function (key, value) {
        $.each(value, function (key, value) {
          if (key === 'title') {
            $('UL#list_movies').append($('<li></li>').text(value));
          }
        });
      });
    });
}
$(document).ready(DocumentReady);
