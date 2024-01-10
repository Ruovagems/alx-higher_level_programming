// 9-script.js

$(document).ready(function () {
  // Use jQuery to fetch data from the provided URL
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Update the text of DIV#hello with the translation
    $('#hello').text(data.hello);
  });
});
