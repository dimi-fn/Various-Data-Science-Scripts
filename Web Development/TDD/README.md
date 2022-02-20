# Test Driven Development (TDD)

Contents
====================

* [Categories of TDD](#categories-of-tdd)
* [Unit Testing with Jest](#unit-testing-with-jest)


-------

TDD is the approach of writing tests with the purpose of passing them correctly.

Tools & Frameworks:
* [Jest](https://jestjs.io/), [Mocha](https://mochajs.org/), [Tape](https://github.com/substack/tape), [Jasmine](https://jasmine.github.io/)

-------

# Categories of TDD

`Unit tests`: e.g. testing a function

`Service tests` (Integration tests, API tests): testing groups of unit tests

`UI tests` (System tests, behaviour tests): when the overall program is tested

-------

# Unit Testing with Jest

Coding files: 

Create your project folder. On git bash and by being under the project directory, run:

* `npm init -y` (or just `npm init`) to initialize the project package
    * this will generate a **package.json** file

* `npm install jest --save-dev`    
    * this will generate a **pagkage-lock.json** file and a **node_modules** directory

* make a `/test` directory. There, create your file to be tested (in this example **fizzbuzz.js**), and the file that will test it, in this case **fizzbuzz.test.js**. I.e., the former file has the form of `<filename.js>` and the latter `<filename.test.js>`
    * e.g. in this example, create a function called 'fizzbuzz' at the fizzbuzz.js file:
        * The fizzbuzz function receives a number as its argument
        * When the number is a multiple of 3 and 5, it returns (“FizzBuzz”)
        * When the number is a multiple of 3, it returns (“Fizz”)
        * When the number is a multiple of 5, it returns (“Buzz”)
        * When the number is not a multiple of 3 or 5, it returns the number itself
    * after the fizzbuzz function, you have to export that as a module:
        * `module.exports = {fizzbuzz}`
    * Now, at the fizzbuzz.test.js file you can import the function and then test it    
