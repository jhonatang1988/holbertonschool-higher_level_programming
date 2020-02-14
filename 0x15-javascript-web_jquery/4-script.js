function DocumentReady () {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('green red');
  });
}
$(document).ready(DocumentReady);
