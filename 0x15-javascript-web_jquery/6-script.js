// 6-script.js

$(document).ready(function () {
  // Use jQuery to handle click event on DIV#update_header
  $('#update_header').click(function () {
    // Update the text of the <header> element to 'New Header!!!'
    $('header').text('New Header!!!');
  });
});

