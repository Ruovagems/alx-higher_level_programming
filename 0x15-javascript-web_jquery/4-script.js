// 4-script.js

$(document).ready(function () {
  // Use jQuery to handle click event on DIV#toggle_header
  $('#toggle_header').click(function () {
    // Toggle the class 'red' and 'green' on the <header> element
    $('header').toggleClass('red green');
  });
});
