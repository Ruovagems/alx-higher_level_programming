// 3-script.js

$(document).ready(function () {
  // Use jQuery to handle click event on DIV#red_header
  $('#red_header').click(function () {
    // Add the class 'red' to the <header> element
    $('header').addClass('red');
  });
});
