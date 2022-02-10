// complete the avg function that takes in an array
// and returns (not console.log) the average (2 rounded digits)


// for calculating the sum of array
let reducer = (previousValue, currentValue) => previousValue + currentValue;
// Complete the function below
const avg = (arr) => {

    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
    average = (arr.reduce(reducer)) / arr.length

    // return average and display that to 2 floating places
    return average.toFixed(2);

}

ar = [7, 19, 33, -5, -99, 6, 12]
console.log(avg(ar)) // => -3.86 (number)
