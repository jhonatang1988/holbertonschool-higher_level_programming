function DocumentReady () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append(function (i, old) {
      return $('<li></li>').text('Item');
    });
  });
}
$(document).ready(DocumentReady);
