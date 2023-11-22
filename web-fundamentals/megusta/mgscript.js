var count = 0;
var contador = document.querySelector("#contador");

function meGusta (){
    count++;
    contador.innerText = count + " Like(s)";
    console.log(count);
}
