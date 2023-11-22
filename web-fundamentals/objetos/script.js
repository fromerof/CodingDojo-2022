// objetos - almacenar informacion.
// ejemplo del taco


var tacos = {
    "carneAsada": "carne con cebolla",
    "Pollo": "Pollo con aji verde",
    "veggie": "Fajita con fajita",
    "tacoInfo": function() {
        console.log("Taco 1: " + tacos.carneAsada);
        console.log("Taco 2: " + tacos.Pollo);
        console.log("Taco 3: " + tacos.veggie);
    } 
}
tacos.tacoInfo();