function DocumentReady () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr',
    function (data) {
      console.log(data);
      $('DIV#hello').text(data.hello);
    });
}
$(document).ready(DocumentReady);
