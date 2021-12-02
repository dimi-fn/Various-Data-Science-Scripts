// comment

/*
multi-line comment
*/

// variable declaration
var x = 10;
let y = 10;

// naming a variable
var firstName = "Alex";

// constants
const TAX_RATE = 22;

// print
console.log(x, firstName)

console.log("Type of x is: " + typeof(x))

console.log("x= " + x + " and first name is: " + firstName)

// floor division
console.log(Math.floor(10/3))

// classes
class Car{
    constructor(brand, colour){
        this.brand = brand;
        this.colour = colour;
    }

    print_output(){
        console.log ("Brand of car is " + this.brand + " and the colour is " + this.colour)
    }
}

result = new Car("mercedes", "black");
result.print_output()