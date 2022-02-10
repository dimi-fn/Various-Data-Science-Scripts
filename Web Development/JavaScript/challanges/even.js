// Using the modulo operator
// complete the function called even that takes in an integer
// and returns (not console.log) a boolean

// Complete the function below
const even = num => {

    if (num % 2 == 0){
        return true
    } else {
        return false
    }

}

console.log(even(3)) // => false
console.log(even(4)) // => true
