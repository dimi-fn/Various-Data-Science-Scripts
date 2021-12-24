# JavaScript

Contents
=======================

* [Data Types](#data-types)
* [Properties](#properties)
* [Methods](#methods)
* [Variables](#variables)
* [Operators](#operators)


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