// complete the function called howManyEvens that takes in an integer and returns (not console.log) how many even numbers are in the array 

// Complete the function below
const howManyEvens = arr => {

    let count=0;
    // You will need to define result
    for (let i = 0; i< arr.length; i++){
        if ((arr[i])%2==0){
            count +=1;
        }
    }
    return count;
  }
  
  
  ar = [7, 19, 33, -5, -99, 6, 12]
  console.log(howManyEvens(ar)) // =? 2
