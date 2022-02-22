/* 
* import the function to be tested
* you put the file to be tested as a directory, hence fizzbuzz and not fizzbuzz.js
*/

const myFunc = require('./fizzbuzz');

describe("Fizzbuzz unit testing", () => {

    // either 'test' or 'it'
    test("test if number is muliple of 3 and 5 then return 'FizzBuzz'", ()=>{
        expect(myFunc.fizzbuzz(30)).toEqual("FizzBuzz");
    })

    test("test if number is muliple of 3 then return 'Fizz'", ()=>{
        expect(myFunc.fizzbuzz(6)).toEqual("Fizz");
    })

    test("test if number is muliple of 5 then return 'Buzz'", ()=>{
        expect(myFunc.fizzbuzz(25)).toEqual("Buzz");
    })

    test("test that any other case returns the input itself", ()=>{
        expect(myFunc.fizzbuzz(31)).toEqual(31);
    })

});
