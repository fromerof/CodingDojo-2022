
function alerta() {
    alert("Wait a few seconds to start the download...");
}

function cambiarImagen() {
    var imagen = document.querySelector(".main-image");
    imagen.remove();
}

function cambiarNombre () {
    var nombre = document.querySelector("h1");
    nombre.innerText = "Thanks, you've been hacked. Have a nice day.";
}