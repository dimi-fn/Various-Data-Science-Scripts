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

// String concatenation
console.log('middle' + ' ' + 'space'); 

// Properties
console.log("hello".length);

// Methods
console.log('hello'.toUpperCase()); // Prints 'HELLO'
console.log('Hey'.startsWith('H')); // Prints true
console.log('    Remove whitespace   '.trim()); // Removes the whitespace at the beginning and end of the string

// Built-in Objects
console.log(Math.floor(10/3)) // takes a decimal number, and rounds down to the nearest whole number
console.log(Math.floor(Math.random() * 50)+ "\n"); // Prints a random whole number between 0 and 50
console.log(Number.isInteger(2017))

// Variables
var x=5;
console.log(x);