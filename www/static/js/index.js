var time = 1000;
var control;

$(document).ready(function(){
  
  muestrear();
  control = setInterval(muestrear, time);

});

$( "#periodo-select" ).change(function() {
  time = $(this).val();
  console.log(time);
  clearInterval(control);
  control = setInterval(muestrear, time);
});

$(window).on("unload", function(e) {
  $.get("/exit", function(data){
      console.log(data);
  });
});

function muestrear(){
  $.get("/samples", function(data) {
    $("#ultima-temperatura").html(data[0] + "°C");
    $("#ultima-humedad").html(data[1] + "%");
    $("#ultima-presion").html(data[2] + " hPa");
    $("#ultima-viento").html(data[3] + " km/h");

    $("#promedio-temperatura").html(data[4] + "°C");
    $("#promedio-humedad").html(data[5] + "%");
    $("#promedio-presion").html(data[6] + " hPa");
    $("#promedio-viento").html(data[7] + " km/h");
  });
}