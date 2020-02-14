function DocumentReady () {
  $('DIV#update_header').click(function () {
    $('header').text("New Header!!!");
  });
}
$(document).ready(DocumentReady);
