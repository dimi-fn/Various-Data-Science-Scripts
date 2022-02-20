const fizzbuzz = (n) => {
    if (n % 3 == 0 && n%5 ==0) {
        return "FizzBuzz";
    }  
    else if (n%3==0){
        return "Fizz";
    }
    else if (n%5==0){
       return "Buzz";
   }
   else {
       return n;
   }
   }
   
// export the function to be tested as a module
module.exports= {fizzbuzz};

/*
module.exports= {
    fizzbuzz:fizzbuzz,
    another_function : another_function
    ...
}
*/
