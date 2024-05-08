$(document).ready(function () {
  function fetchHello() {
    var languageCode = $('#language_code').val();
    var url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(function () {
    fetchHello();
  });

  $('#language_code').keypress(function (event) {
    if (event.key === 'Enter') {
      fetchHello();
    }
  });
});
