function DocumentReady () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append($('<li></li>').text('Item'));
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').children().remove();
  });

  $('DIV#remove_item').click(function () {
    $('UL.my_list').children().last().remove();
  });
}
$(document).ready(DocumentReady);
