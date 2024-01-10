// 7-script.js

$(document).ready(function () {
  // Use jQuery to fetch data from the provided URL
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Update the text of DIV#character with the character name
    $('#character').text(data.name);
  });
});
