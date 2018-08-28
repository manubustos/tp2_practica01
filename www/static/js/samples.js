$(document).ready(function(){

  setInterval(muestrear, 1000);
  //muestrear();

});

function muestrear(){
  $.get("/samples/" + id_sample, function(data) {
    $("#ultima-temperatura").html(data.temperature + "°C");
    $("#ultima-humedad").html(data.humidity + "%");
    $("#ultima-presion").html(data.pressure + " hPa");
    $("#ultima-viento").html(data.windspeed + " km/h");
  });

  promedio();
}

function promedio() {

  $("#promedio-temperatura").html(temperatura + "°C");
  $("#promedio-humedad").html(humedad + "%");
  $("#promedio-presion").html(presion + " hPa");
  $("#promedio-viento").html(viento + " km/h");
}
