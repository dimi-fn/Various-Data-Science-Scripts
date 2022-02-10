// Complete the info function that takes in an array
// and returns information about the array

const info = arr => {

    // sum of array
    const reducer = (previousValue, currentValue) => previousValue + currentValue;

    // counts evens
    let count_evens=0;
    for (let i = 0; i< arr.length; i++){
        if ((arr[i])%2==0){
            count_evens +=1;
        }
    }

    return {
        "array" : arr,
        "elements": arr.length,
        "avg":  arr.reduce(reducer) /arr.length,
        "sum": arr.reduce(reducer),
        "howManyEvenNumbers" : count_evens,
    };
};


console.log(info([1, 2, 3, 4, 5, 6, 7, 8, 9]))
/* 
When passed the array above the result should like it does below:
{
  array: [
    1, 2, 3, 4, 5,
    6, 7, 8, 9
  ],
  elements: 9,
  avg: 5,
  sum: 45,
  howManyEvenNumbers: 4,

}
*/
