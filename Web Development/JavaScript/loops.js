/* Loops */
for (let counter = 0; counter < 4; counter++) {
    console.log(counter);
}

/* In python it would be
for i in range (0,4):
    print(i)
    i+=1 # prints 0,1,2,3
*/    

//reverse loop
for (let counter = 3; counter >= 0; counter--){
    console.log(counter);
  }

// iterate arrays
const vacationSpots = ['Amsterdam', 'Copenhagen', 'Paris'];

// Write your code below
for (let i = 0; i < vacationSpots.length; i++ ){
  console.log('I would love to visit ' + vacationSpots[i]);
}

/* 
In python:

vacationSpots = ['Amsterdam', 'Copenhagen', 'Paris']
for city in vacationSpots:
    print(city)
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