
var solicitudCount = 2;
var conexiones = 500;
function changeName (){
    var cambiarNombre = document.querySelector("#nombreUser");
    cambiarNombre.innerText = "Elon Musk";
}

function aceptar(){
    solicitudCount--;
    var contador = document.querySelector(".circle");
    contador.innerText = solicitudCount;
    conexiones++;
    var contador = document.querySelector(".circle1");
    contador.innerText = conexiones;
    var remover = document.querySelector(".solicitud1")
    remover.remove();
}
function quitar(){
    solicitudCount--;
    var contador = document.querySelector(".circle");
    contador.innerText = solicitudCount;
    var remover = document.querySelector(".solicitud1")
    remover.remove();
}
function aceptar2(){
    solicitudCount--;
    var contador = document.querySelector(".circle");
    contador.innerText = solicitudCount;
    conexiones++;
    var contador = document.querySelector(".circle1");
    contador.innerText = conexiones;
    var remover = document.querySelector(".solicitud2")
    remover.remove();
}
function quitar2(){
    solicitudCount--;
    var contador = document.querySelector(".circle");
    contador.innerText = solicitudCount;
    var remover = document.querySelector(".solicitud2")
    remover.remove();
}
