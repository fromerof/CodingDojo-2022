function fibonacciArray(n) {
    // [0, 1] son los valores inciales del arreglos para calcular el resto
    var fibArr = [0, 1];
    var sum = 0;
    for (var i = 0; i < n -2; i++){
        sum = fibArr[i] + fibArr[i + 1];
        fibArr.push(sum);
    }
    // tu código aquí
    return fibArr;
}
var result = fibonacciArray(10);
console.log(result); // esperamos de vuelta[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]