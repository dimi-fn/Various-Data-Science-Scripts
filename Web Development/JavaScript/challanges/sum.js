// complete the sum function that takes in an array
// and returns (not console.log) the sum of its elements

// Complete the function below
const reducer = (previousValue, currentValue) => previousValue + currentValue;
const sum = (arr) => {
    
    /* reduce()
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
    */
    return arr.reduce(reducer);
}

ar = [7, 19, 33, -5, -99, 6, 12]
console.log(sum(ar)) //=> -27


const sum_with_for = (arr) => {
    
    let sum = 0;
    for (i=0; i<arr.length; i++){
        sum += arr[i];
    }
    return sum;
}

ar = [7, 19, 33, -5, -99, 6, 12]
console.log(sum(ar)) //=> -27
