var count = 1;
var countElement = document.querySelector("#count");

function add(){
    count++;
    countElement.innerText = "The count is " + count;
}

function substract(){
    count--;
    countElement.innerText = "The count is " + count;
}