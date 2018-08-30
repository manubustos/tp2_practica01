$(document).ready(function(){

  muestrear();
  setInterval(muestrear, 1000);

});

function muestrear(){
  ulitmo();
  promedio();
}

function ulitmo(){
  $.get("/last", function(data) {
    $("#ultima-temperatura").html(data[0] + "°C");
    $("#ultima-humedad").html(data[1] + "%");
    $("#ultima-presion").html(data[2] + " hPa");
    $("#ultima-viento").html(data[3] + " km/h");
  });
}

function promedio() {
  $.get("/average", function(data) {
    $("#promedio-temperatura").html(data[0] + "°C");
    $("#promedio-humedad").html(data[1] + "%");
    $("#promedio-presion").html(data[2] + " hPa");
    $("#promedio-viento").html(data[3] + " km/h");
  });
}
