if(localStorage.theme) {
  $("link[id='styles']").attr('href', localStorage.theme);
  if (localStorage.theme == "https://maxcdn.bootstrapcdn.com/bootswatch/4.5.0/journal/bootstrap.min.css") {
    $("input[id='customSwitch1']").prop('checked', false);
  }
}

$('#customSwitch1').click(function () {
  if ($("link[id='styles']").attr('href') == 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/journal/bootstrap.min.css'){
    $("link[id='styles']").attr('href', 'https://maxcdn.bootstrapcdn.com/bootswatch/4.5.0/darkly/bootstrap.min.css');
    localStorage.theme = "https://maxcdn.bootstrapcdn.com/bootswatch/4.5.0/darkly/bootstrap.min.css";
    $("input[id='customSwitch1']").prop('checked', true);
  } else {
    $("link[id='styles']").attr('href', 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/journal/bootstrap.min.css');
    localStorage.theme = "https://maxcdn.bootstrapcdn.com/bootswatch/4.5.0/journal/bootstrap.min.css";
    $("input[id='customSwitch1']").prop('checked', false);
  }
});
