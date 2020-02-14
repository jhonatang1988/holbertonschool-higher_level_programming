function DocumentReady () {
  let code = '';
  $('INPUT#btn_translate').click(function () {
    code = $('INPUT#language_code').val();
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + code,
      function (data) {
        $('DIV#hello').text(data.hello);
      });
  });
}
$(document).ready(DocumentReady);
