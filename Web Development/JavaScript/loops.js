/* Loops */
for (let counter = 0; counter < 4; counter++) {
    console.log(counter);
    /* In python it would be:
    for i in range (0,4):
      print(i)
      i+=1 # prints 0,1,2,3
    */  
}
console.log("\n");  

// reverse loop
for (let counter = 3; counter >= 0; counter--){
    console.log(counter);
    /* In python it would be:
    i=4
    while i>=1:
      i-=1
      print(i)
    */
  }
console.log("\n");

// iterate arrays
const vacationSpots = ['Amsterdam', 'Copenhagen', 'Paris'];
for (let i = 0; i < vacationSpots.length; i++ ){
  console.log('I would love to visit ' + vacationSpots[i]);
}
console.log("\n");
/*
In python:
vacationSpots = ['Amsterdam', 'Copenhagen', 'Paris']
for city in vacationSpots:
    print('I would love to visit {}'.format(city))
*/

// nested loops
const myArray = [10, 20, 30];
const yourArray = [30, 40, 50];
for (let i = 0; i < myArray.length; i++) {
  for (let j = 0; j < yourArray.length; j++) {
    if (myArray[i] === yourArray[j]) {
      console.log('Both loops have the number: ' + yourArray[j])
    }
  }
};

// while loop
// A for loop that prints 1, 2, and 3
for (let counterOne = 1; counterOne < 4; counterOne++){
    console.log(counterOne);
  }
   
  // A while loop that prints 1, 2, and 3
  let counterTwo = 1;
  while (counterTwo < 4) {
    console.log(counterTwo);
    counterTwo++;
  }

// do..while (runs at least one time)  
let countString = '';
let i = 0;
do {
  countString = countString + i;
  i++;
} while (i < 5);
console.log(`the value of countString is: ${countString}`);
console.log("\n");

// break statement
for (let i = 0; i < 99; i++) {
    if (i > 2 ) {
       break;
    }
    console.log('I am smaller than 2');
  }   
  console.log('Loop broke because I am the number 3');
  /*
  In Python:
  for i in range(0,100):
  print("I'm smaller than 2")
  if i==2:
    print("Loop broke because I am the number 3")
    break
  */
