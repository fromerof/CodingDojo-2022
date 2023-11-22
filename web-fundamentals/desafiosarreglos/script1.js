function alwaysHungry(arr) {
    for (var i = 0; i < arr.length; i++) {
        var count = 0;
        if (arr[i] == "comida"){
            console.log("delicioso");
            count++;
        }
    }
    if (count == 0) {
        console.log("Tengo Hambre");
    }
}
alwaysHungry([3.14, "comida", "pastel", true, "comida"]);
alwaysHungry([4, 1, 5, 7, 2]);
