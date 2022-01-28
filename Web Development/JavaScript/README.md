# JavaScript

Contents
=======================

* Coding files: [general](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/general.js), [conditionals](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/conditionals.js), [arrays](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/arrays.js), [loops](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/loops.js), [functions](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/functions.js), [iterators](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/Iterators.js), [objects & methods](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/objects_methods.js), [advanced objects](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/advanced_objects.js)
* [Data Types](#data-types)
* [Properties](#properties)
    * [Arrays](#arrays)
* [Variables](#variables)
* [Operators](#operators)
* [Loops](#loops)
* [Functions](#functions)
    * [Parameters & Arguments](#parameters--arguments)
    * [Default Parameters](#default-parameters)
    * [Functions as Parameters](#functions-as-parameters)
    * [Helper Functions](#helper-functions)
    * [Function Expressions](#function-expressions)
    * [Arrow Functions](#arrow-functions)
        * [Concise Body Arrow Functions](#concise-body-arrow-functions)
    * [Iterators](#iterators)
* [Blocks & Scope](#blocks--scope)
    * [Scope Pollution](#score-pollution)
* [Objects & Methods](#objects--methods)
    * [Advanced Objects](#advanced-objects)
        * [Privacy](#privacy)
        * [Getters & Setters](#getters--setters)
        * [Factory Functions](#factory-functions)
        * [Built-in Methods](#built-in-methods)
* Cheatsheets from codeacademy
    * [Intro](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-introduction/cheatsheet)
    * [Conditionals](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-control-flow/cheatsheet)
    * [Arrays](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-arrays/cheatsheet), [more on arrays by MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    * [Loops](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-iterators/cheatsheet)
    * [Functions](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-functions/cheatsheet) 
    * [Iterators](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-iterators/cheatsheet)
    * [Scope](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-scope/cheatsheet)
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

[Coding file](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/arrays.js)

* Data structure used to store lists of data.
    * Arrays are mutable (the array values can be changed), ordered, stored data.

* [Arrays](https://www.codecademy.com/learn/paths/introduction-to-javascript/tracks/introduction-to-javascript/modules/learn-javascript-arrays/cheatsheet)
    * some of the built-in methods: 
        * `.push()`: it adds new element in the end of array
        * `.pop()`: it removes the last element
        * `.slice()`: it extracts a section (range) of the array
        * `.shift()`: it removes the first element
        * `.unshift()`: it introduces new element in the beginning of array. The previous array[0] now automatically becomes array[1]
        *  `.join()`, `.slice()`, `.splice()`, `.concat()`
        * [more array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

-----

# Variables

* [var vs let](https://stackoverflow.com/questions/762011/whats-the-difference-between-using-let-and-var)
* [let vs var vs const](https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/)
* [let vs var vs const](https://ui.dev/var-let-const/#:~:text=Turns%20out%2C%20const%20is%20almost,it%20to%20a%20new%20value.)
* `undefined`: if a variable is declared without a value, then the variable's value will automatically be assigned as undefined
* `const`: constant variable, i.e. the variable's value cannot change

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

# Loops

[Coding file](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/loops.js)

In **Python**, e.g. this:

    for i in range (0,4):
        print(i)
        i+=1 # prints 0,1,2,3

The equivalent in **Javascript** can be:

    for (let counter = 0; counter < 4; counter++) {
        console.log(counter);
    }

More at [loops.js](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/loops.js)    

------

# Functions
In JavaScript, [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) are first class objects, i.e. they have properties and methods.
* we can also pass functions into other functions as parameters

A function declaration consists of:

* The function keyword
* The name of the function (i.e. the `identifier`) followed by parentheses 
* A function body (the block of statements required to perform a specific task) enclosed in the function’s curly brackets, `{ }`.

        function printHi(){
            console.log("Hi")
        }
        printHi();

In Python, the above would be:

        def printHi():
            return("Hi")
        printHi()  

## Parameters & Arguments

Functions receive inputs and they use the inputs to perform a task. When declaring a function, we can specify its `parameters`, which allow functions to accept **inputs** and perform a task using those inputs. Parameters are used as placeholders for information that will be passed to the function when it is called.

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

## Functions as Parameters
* We can pass functions into other functions as parameters

* A **higher-order function** is a function that either accepts functions as parameters, returns a function, or both

* `callback function`: a callback function is a function passed as an argument into another function
    * when we pass a function in as an argument to another function, we don’t invoke it. <ins>Invoking the function would evaluate to the return value of that function call</ins>. With **callbacks**, we pass in the function itself by typing the function name **without the parentheses**

## Helper Functions
The **return** value of a function can be used into another function via `function declaration`. In this case, the latter function can be called a `helper function`.

E.g.:

    function multiplyByNineFifths(number) {
    return number * (9/5);
    };
    
    function getFahrenheit(celsius) {
    return multiplyByNineFifths(celsius) + 32;
    };
    
    getFahrenheit(15); // Returns 59

## Function Expressions

Another way to define a function is to use a function expression. To define a function inside an expression, we can use the function keyword. In a function expression, the function name is usually omitted. A function with no name is called `anonymous`. A function expression is often stored in a variable in order to refer to it.

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

* when 2 or more parameters:
    *  `const functionName = (param1, param2) => {};`

E.g.:

Instead of: 

    const squareNum = (num) => {
    return num * num;
    };

You can do:

    const squareNum = num => num * num; // via callback

-------

## Iterators

[Coding file](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/Iterators.js)

Some of the iterator methods:

* `.forEach()`: it executes the same code for each element of an array
* `.map()`: it takes an argument of a callback function and returns a new array
* `.filter()`: it returns an array of elements after filtering out certain elements from the initial array
* `.findIndex()`: it returns the index of the first element that evaluates to true in the callback function.
    * If there isn’t a single element in the array that satisfies the condition in the callback, then .findIndex() will return -1.
* `.reduce()`: it returns a single value after iterating through the elements of an array, thereby reducing the array

<br>

* [Array iteration methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#Iteration_methods)

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

# Objects & Methods

[Coding file](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/objects_methods.js)

<br>

**Objects**:

* Objects can be assigned to variables just like any JavaScript type
* They are like dictionaries in Python
    * Objects store collections of key-value pairs:
        * `key` (**identifier**, **property name**)
        * `key value`
            * the key-value pairs comprise the **properties** of the object literals
* Hence, each key-value pair is a property, and when a property is a function it is known as a method
*  Objects are **mutable** meaning we can update them after we create them, even when they are declared with const

<br>

    let objectLiteral = {
    "first_key": "value_of_first_key",
    "second_key": "value_of_second_key"
    };

*  `nested objects`: an object might have another object as a property which in turn could have a property that’s an array of even more objects    

<br>

**Pass by Reference**:

Objects are passed by reference
* This means when we pass a variable assigned to an object into a function as an argument, the computer interprets the parameter name as pointing to the space in memory holding that object. As a result, functions which change object properties actually mutate the object permanently (even when the object is assigned to a const variable).

**Looping through Objects**:

* [Iterating through objects with the for..in syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
    * for...in will execute a given block of code for each property in an object

------

**Methods**:

Methods are actions we can perform. We can call methods by appending an instance with:
* a period (the dot operator)
* the name of the method
* opening and closing parentheses

Hence, when the data stored on an object is a function, we call that a *method*.
* A property is what an object has, while a method is what an object does. For example:
    * `console.log()`:
        * `console` is a global javascript object
        * `.log` is a method of that object, i.e., it is about what that object (console) does

------

## Advanced Objects

[Coding file](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/advanced_objects.js)

Objects are collections of related data and functionality
* That functionality can be stored via *methods* on *objects*

Avoid using *arrow functions* when using the `this` in a method
* Arrow functions inherently bind, or tie, an already defined this value to the function itself that is not the calling object
* [global objects](https://developer.mozilla.org/en-US/docs/Glossary/Global_object), [arrow function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

------

### Privacy
The privacy with regard to accessing and updating object properties is about the idea that only certain properties should be mutable or able to change in value. In JavaScript, the *naming convention* `_` (underscore) is used before the name of a property to imply that the property should not be altered

------

### Getters & Setters

**Getters**: Getters are methods that get and return the internal properties of an object
* they can perform an action on the data when getting a property
* they can return different values using conditionals
* in a getter, we can access the properties of the calling object using `this`.

N.b. It is still possible to reassign properties with `._variable`

<br>

**Setters**:

Setters reassign values of existing properties within an object. Like getter methods, there are similar advantages to using setter methods that include:
* checking input
* performing actions on properties
* displaying a clear intention for how the object is supposed to be used

N.b. It is still possible to reassign properties with `._variable`

------

### Factory Functions
A factory function is a function that returns an object and can be *reused* to make *multiple* object *instances*. Factory functions can also have parameters allowing us to customize the object that gets returned (rememeber using `self` in classes via Python)
* you can also use the technique of `property value shorthand`, which is a shortcut for assigning properties to variables, see the [respective coding file](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/JavaScript/advanced_objects.js) for an example
* you can also make use of the `destructured assignment`, i.e. by creating a variable with the name of an object’s key that is wrapped in curly braces { } and assign to it the object

------

### Built-in Methods

The are available various object instance methods like:
* `.hasOwnProperty()`, `.valueOf()`
* [object classes: object instance documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#Methods)
   * .e.g.: [.Object.keys()](), [.Object.entries()]()