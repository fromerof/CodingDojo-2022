function user(element){
    var count = Number(element.previousElementSibling.innerText) + 1;
    element.previousElementSibling.innerText = count;
}