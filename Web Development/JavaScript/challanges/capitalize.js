// complete the function capitalize that takes in a word and returns a capitalised string

// Complete the function below
const capitalizeAll = (word) => {

    // You will have to define the variable
    return word.toUpperCase();
  }
  
  
  console.log(capitalizeAll("hELLo")) // => HELLO
  console.log(capitalizeAll("betH")) // => BETH
  console.log(capitalizeAll("jaGaN")) // => JAGAN
  console.log(capitalizeAll("sergI")) // => SERFI



function capitalize(string) {
      // capitalize the first letter, lowercase for the rest
    return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
}

console.log(capitalize("heLLo")) // => Hello
