function DocumentReady () {
  $('DIV#red_header').click(function () {
    $('header').addClass('red');
  });
}
$(document).ready(DocumentReady);
