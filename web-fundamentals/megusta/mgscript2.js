var userCount = 0;
var userCount2 = 0;
var userCount3 = 0;
var countArr = [];
var contador1 = document.querySelector(".contador1");
var contador2 = document.querySelector(".contador2");
var contador3 = document.querySelector(".contador3");


function user1(){
    userCount++;
    countArr[0] = (userCount);
    contador1.innerText = userCount + " Like(s)";
    console.log(countArr);
}

function user2(){
    userCount2++;
    countArr[1] = (userCount2);
    contador2.innerText = userCount2 + " Like(s)";
    console.log(countArr);
}
function user3(){
    userCount3++;
    countArr[2] = (userCount3);
    contador3.innerText = userCount3 + " Like(s)";
    console.log(countArr);
}
