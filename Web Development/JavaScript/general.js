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
console.log("\n");

/* String concatenation */
console.log('String' + ' ' + 'concatenation'); 
console.log("\n");

/* String Interpolation */
var x = "interpolation";
console.log(`This is about string ${x}`); // In python this would be: print("This is about string {}".format(x))
console.log("\n");

/* Properties */
let h = "hello";
console.log(`The length of hello is: ${h.length}`);
console.log("\n");

/* Methods */
console.log('hello'.toUpperCase()); // Prints 'HELLO'
console.log('Hey'.startsWith('H')); // Prints true
console.log('    Remove whitespace   '.trim()); // Removes the whitespace at the beginning and end of the string
console.log("\n");

/* Built-in Objects */
console.log(Math.floor(10/3)) // takes a decimal number, and rounds down to the nearest whole number
console.log(Math.floor(Math.random() * 50)+ "\n"); // Prints a random whole number between 0 and 50
console.log(Number.isInteger(2017))
console.log("\n");

/***************** Variables *****************/
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
console.log("\n");

/* Operators */
var x=1;
x+=1
console.log(x);

x++ // x+=1 == x++
console.log(x);

/***************** Operators *****************/
//typeof, in Python it would be type()
var x = 1;
var y = "dog";
var z = true;
console.log(`Type of "${x}" is: ${typeof x}`);
console.log(`Type of "${y}" is: ${typeof y}`);
console.log(`Type of "${z}" is: ${typeof z}`);  

