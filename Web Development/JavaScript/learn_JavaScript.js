// this is a comment

/*
this is
a multi-line comment
*/

//print to the console
console.log(3);
console.log(3+4);
console.log("the remainder of 13/4 is: "+13%4);
console.log(/*you can put comments even here*/5);
console.log("this is JavaScript!");

/* String concatenation */
console.log('middle' + ' ' + 'space'); 

/* String Interpolation */
var x = "dogs";
console.log(`I love ${x}`); // In python this would be: print("I love {}".format(x))

/* Properties */
console.log("hello".length);

/* Methods */
console.log('hello'.toUpperCase()); // Prints 'HELLO'
console.log('Hey'.startsWith('H')); // Prints true
console.log('    Remove whitespace   '.trim()); // Removes the whitespace at the beginning and end of the string

/* Built-in Objects */
console.log(Math.floor(10/3)) // takes a decimal number, and rounds down to the nearest whole number
console.log(Math.floor(Math.random() * 50)+ "\n"); // Prints a random whole number between 0 and 50
console.log(Number.isInteger(2017))

/* Variables */
var x=5;
console.log("the value of x is:", x);

let w=6;
console.log(w);

// undefined variable
let price;
console.log(price); // Output: undefined
price = 350; // change the value of price
console.log(price); // Output: 350

// constant variable
const myName = "James";
console.log(myName);

/* Operators */
var x=1;
x+=1
console.log(x);

x++ // x+=1 == x++
console.log(x);


/* Operators */
//typeof, in Python it would be type()
var x = 1;
var y = "dog";
var z = true;
console.log(`Type of "${x}" is: ${typeof x}`);
console.log(`Type of "${y}" is: ${typeof y}`);
console.log(`Type of "${z}" is: ${typeof z}`);


/* Conditionals: if statements, switch */
if (false) {
    console.log('The code in this block will not run.');
  } else {
    console.log('But the code in this block will!');
  }

  let isNightTime = true;
  if (isNightTime) {
    console.log('Turn on the lights!');
  } else {
    console.log('Turn off the lights!');
  }
// the above is equal with the below one (using ternary operator)
isNightTime ? console.log('Turn on the lights!') : console.log('Turn off the lights!');

// switch 
let athleteFinalPosition = 'first place';

switch(athleteFinalPosition){
  case 'first place':
    console.log('You get the gold medal!');
    break;
  case 'second place':
    console.log('You get the silver medal!');
    break;
  case 'third place':
    console.log('You get the bronze medal!');
    break;
  default: // it is like else:
    console.log('No medal awarded.');
    break;
}

/* Functions */

function printHi(){
    console.log("Hi")
}
printHi();

/* In Python it would be:
def printHi():
    return("Hi")
printHi()  
*/

function rectangleArea(width, height) {
    if (width < 0 || height < 0) {
      return 'You need positive integers to calculate area!';
    }
    return width * height;
  }
console.log(rectangleArea(5,-1));

// you can also assign the function's result into a variable:
var result = rectangleArea(5,-1);
console.log(result);

// Helper Functions ~ function declarations
function multiplyByNineFifths(number) {
    return number * (9/5);
    };
    
function getFahrenheit(celsius) {
return multiplyByNineFifths(celsius) + 32;
};

console.log(getFahrenheit(15)); // Returns 59

// Function Expressions

const isWeekend = function(day){
    if (day==="Saturday" || day==="Sunday"){
      return "Yea! It is " + day + ", so it is weekend!";
    } else {
      return "It is a weekday because it is " + day;
    }
  };
  
  isWeekend("Tuesday")
  console.log(isWeekend('Tuesday'));

  isWeekend("Sunday")
  console.log(isWeekend('Sunday'));

  // Arrow Functions
  const rectangle_Area = (width, height) => {
    let area = width * height;
    return area;
  };
  console.log(rectangle_Area(5,3));
