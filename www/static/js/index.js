$(document).ready(function(){

  setInterval(muestrear, 1000);
  //muestrear();

});

function muestrear(){
  $.get("/samples/last/", function(data) {
    $("#ultima-temperatura").html(data[0] + "°C");
    $("#ultima-humedad").html(data[1] + "%");
    $("#ultima-presion").html(data[2] + " hPa");
    $("#ultima-viento").html(data[3] + " km/h");
  });

  promedio();
}

function promedio() {

  $("#promedio-temperatura").html(temperatura + "°C");
  $("#promedio-humedad").html(humedad + "%");
  $("#promedio-presion").html(presion + " hPa");
  $("#promedio-viento").html(viento + " km/h");
}
