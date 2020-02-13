function DocumentReady () {
  $('DIV#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
}
$(document).ready(DocumentReady);
