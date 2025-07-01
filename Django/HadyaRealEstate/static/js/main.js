const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

$$(document).ready(function() {
  setTimeout(function() {
    $('#message').fadeOut('fast');
  }, 500); // Adjust delay time if needed
});
