$(document).ready(function(){

  $("#ultima-temperatura").html(temperatura + "°C");
  $("#ultima-humedad").html(humedad + "%");
  $("#ultima-presion").html(presion + " hPa");
  $("#ultima-viento").html(viento + " km/h");

  $("#promedio-temperatura").html(temperatura + "°C");
  $("#promedio-humedad").html(humedad + "%");
  $("#promedio-presion").html(presion + " hPa");
  $("#promedio-viento").html(viento + " km/h");
});


function promedio() {
  $.get("/", function() {
    $("#promedio-temperatura").html(temperatura);
    $("#promedio-humedad").html(humedad);
    $("#promedio-presion").html(presion);
    $("#promedio-viento").html(viento);
  });
}

function ultima() {

}