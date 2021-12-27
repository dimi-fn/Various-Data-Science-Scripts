# JavaScript

Contents
=======================

* Coding files: [general](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/general.js), [conditionals](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/conditionals.js), [loops](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/loops.js), [functions](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/functions.js)
* [Data Types](#data-types)
* [Properties](#properties)
    * [Arrays](#arrays)
* [Methods](#methods)
* [Variables](#variables)
* [Operators](#operators)
* [Functions](#functions)
    * [Parameters & Arguments](#parameters--arguments)
    * [Default Parameters](#default-parameters)
    * [Helper Functions](#helper-functions)
    * [Function Expression](#function-expression)
    * [Arrow Functions](#arrow-functions)
        * [Concise Body Arrow Functions](#concise-body-arrow-functions)
* [Blocks & Scope](#blocks--scope)
    * [Scope Pollution](#score-pollution)
* [Loops](#loops)
* Cheatsheets from codeacademy
    * [Intro](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-introduction/cheatsheet)
    * [Conditionals](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-control-flow/cheatsheet)
    * [Functions](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-functions/cheatsheet) 
    * [Scope](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-scope/cheatsheet)
    * [Arrays](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-arrays/cheatsheet)
    * [Loops](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-iterators/cheatsheet)
    * [Objects](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-objects/cheatsheet)
-----

# Data Types

In JavaScript, there are seven fundamental data types:
* `number`
* `string`
* `boolean`
* `null`
* `undefined`
    * It's denoted by the keyword undefined (without quotes). It also represents the absence of a value though it has a different use than null
* `symbol`
    * Symbols are unique identifiers
* `object`
    * Collections of related data

The first 6 (all data types apart from the object) are considered **primitive** data types

-----

# Properties

E.g.

* length
    * `console.log("hello".length);`

## Arrays

[Arrays](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-arrays/cheatsheet)

-----

# Methods

Methods are actions we can perform. We can call methods by appending an instance with:
* a period (the dot operator)
* the name of the method
* opening and closing parentheses

-----

# Variables

* [var vs let in JavaScript](https://stackoverflow.com/questions/762011/whats-the-difference-between-using-let-and-var)
* if a variable is declared without a value, then the variable's value will automatically be assigned as `undefined`
* constant variable (the variable's value cannot change): `const`

-----

# Operators

* `typeof`
* `ternary operator`
    * e.g., the following:

            let isNightTime = true; 
            if (isNightTime) {
            console.log('Turn on the lights!');
            } else {
            console.log('Turn off the lights!');
            }

    is the same with the below one, using `ternary` operator instead:

        isNightTime ? console.log('Turn on the lights!') : console.log('Turn off the lights!');   

-----

# Functions

A function declaration consists of:

* The function keyword
* The name of the function, or its `identifier`, followed by parentheses 
* A function body, or the block of statements required to perform a specific task, enclosed in the function’s curly brackets, `{ }`.

        function printHi(){
            console.log("Hi")
        }
        printHi();

In Python, the above would be:

        def printHi():
            return("Hi")
        printHi()  

## Parameters & Arguments

Functions receive inputs and they use the inputs to perform a task. When declaring a function, we can specify its `parameters`, which allow functions to accept inputs and perform a task using those inputs. Parameters are used as placeholders for information that will be passed to the function when it is called.

    function functionName (parameters){
        inputs;
        }
    // call the function
    functionName(arguments)    

## Default Parameters
Default parameters allow parameters to have a predetermined value in case there is no argument passed into the function or if the argument is `undefined` when called.

Below for example, if a name is given (i.e. if an argument is passed into the function) then that name will be printed, otherwise the default parameter

    function greeting (name = 'stranger') {
    console.log(`Hello, ${name}!`)
    }
    
    greeting('Peter') // Output: Hello, Peter!
    greeting() // Output: Hello, stranger! 

## Helper Functions

The return* value of a function can be used into another function via `function declaration`. In this case, the latter function can be called a `helper function`

E.g.:

    function multiplyByNineFifths(number) {
    return number * (9/5);
    };
    
    function getFahrenheit(celsius) {
    return multiplyByNineFifths(celsius) + 32;
    };
    
    getFahrenheit(15); // Returns 59

## Function Expression    

Another way to define a function is to use a function expression. To define a function inside an expression, we can use the function keyword. In a function expression, the function name is usually omitted. A function with no name is called an *anonymous* function. A function expression is often stored in a variable in order to refer to it.

E.g.:

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

------

## Arrow Functions

ES6 introduced arrow function syntax, a shorter way to write functions by using the special “fat arrow” `() =>` notation.
* Arrow functions remove the need to type the keyword function every time you need to create a function. Instead, you first include the parameters inside the `( )` and then add an arrow `=>` that points to the function body surrounded in `{ }`
* E.g.

### Concise Body Arrow Functions

* when 0 parameters:
    *  `const functionName = () => {};`

* when 1 parameter:
    *  `const functionName = param1 => {};`

* 2 or more parameters:
    *  `const functionName = (param1, param2) => {};`

E.g.:

Instead of: 

    const squareNum = (num) => {
    return num * num;
    };

You can do:

    const squareNum = num => num * num;

-------

# Blocks & Scope

https://www.codecademy.com/learn/introduction-to-javascript/modules/learn-javascript-scope/cheatsheet

* A `block` is the code found inside a set of curly braces `{}`
    * Blocks help us group one or more statements together and serve as an important structural marker for our code
    * `Blocks` define the `scope` of variables

<br>    

`Scope` is the context in which our variables are declared. We think about scope in relation to blocks because variables can exist either outside of or within these blocks
* In global scope, variables are declared `outside of blocks`. These variables are called `global variables`
    * Because global variables are not bound inside a block, they can be accessed by any code in the program, including code in blocks

<br>    

When a variable is defined inside a block, it is only accessible to the code within the curly braces `{}`
We say that variable has `block scope` because it is only accessible to the lines of code within that block.
* these are `local variables`

## Scope Pollution

When you declare global variables, they go to the global namespace. The global namespace allows the variables to be accessible from anywhere in the program. These variables remain there until the program finishes which means our global namespace can fill up really quickly.

`Scope pollution` is when we have too many global variables that exist in the global namespace, or when we reuse variables across different scopes
* Scope pollution makes it difficult to keep track of our different variables and sets us up for potential accidents. For example, globally scoped variables can collide with other variables that are more locally scoped, causing unexpected behavior in our code

<br>

it’s best practice to not define variables in the global scope.

------

# Loops

In Python, e.g. this:

    for i in range (0,4):
        print(i)
        i+=1 # prints 0,1,2,3


In Javascript can be:

    for (let counter = 0; counter < 4; counter++) {
        console.log(counter);
    }

More at [loops.js](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/loops.js)    