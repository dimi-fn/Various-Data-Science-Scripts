# JavaScript

Contents
=======================

* [learn_JavaScript.js](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/learn_JavaScript.js)
* [Data Types](#data-types)
* [Properties](#properties)
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
* [Blocks & Scope](#blocks---scope)

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