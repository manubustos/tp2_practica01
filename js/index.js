$(document).ready(function(){
  $("#ultima-temperatura").html(temperatura);
  $("#ultima-humedad").html(humedad);
  $("#ultima-presion").html(presion);
  $("#ultima-viento").html(viento);

  $("#promedio-temperatura").html(temperatura);
  $("#promedio-humedad").html(humedad);
  $("#promedio-presion").html(presion);
  $("#promedio-viento").html(viento);
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