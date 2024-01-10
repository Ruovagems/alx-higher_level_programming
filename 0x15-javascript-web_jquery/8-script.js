// 8-script.js

$(document).ready(function () {
  // Use jQuery to fetch data from the provided URL
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Iterate through the movies and append titles to UL#list_movies
    $.each(data.results, function (index, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
