/***************************************************** Iterators ********************************************************************************************/

const { all } = require("express/lib/application");

/***************************  Iterate Arrays *******************************************/
var cats = ["Zelda", "Rumble", "Sam"];

for (const catName of cats) {
  console.log(`This cat's name is ${catName}`);
};

/***************************  Iterate Objects *******************************************/
var catData = { name: "Zelda", age: 3, markings: "calico" };

for (const key in catData) {
  console.log(`${key}: ${catData[key]}`);
};

/***************************  forEach *******************************************/
const cars = ["mercedes", "bmw", "audi", "ferrari"];
// Iterator: .forEach()
// 1st way
cars.forEach(function(carItem){
    console.log(`This is a ${carItem} car`);
});
console.log("\n")

// 2nd way with arrow function
cars.forEach(carItem => console.log(`This is a ${carItem} car`));

/***************************  filter() *******************************************/
const randomNumbers = [375, 200, 3.14, 7, 13, 852];
const smallNumbers = randomNumbers.filter(num => {
    if (num<250){
      return num
    };
  })
console.log(smallNumbers);

const favoriteWords = ['nostalgia', 'hyperbole', 'fervent', 'esoteric', 'serene'];
const longFavoriteWords = favoriteWords.filter(word=> {
    if (word.length>7){
      return word
    };
  })
console.log(longFavoriteWords);

/***************************  some() *******************************************/
var cats = ["Zelda", "Rumble", "Sam", "Flora"];
cats.some(catName => catName.endsWith("a")); //=> true

/***************************  every() *******************************************/

var cats = ["Zelda", "Rumble", "Sam", "Flora"];
cats.every(catName => catName.endsWith("a")); //=> false

/***************************  .findIndex() *******************************************/
const animals = ['hippo', 'tiger', 'lion', 'seal', 'cheetah', 'monkey', 'salamander', 'elephant'];

const foundAnimal = animals.findIndex(animal=>{
  // return the index of the elephant animal  
  return animal === "elephant";
});

const startsWithS = animals.findIndex(animal=>{
    // return the index of the first element animal that starts with 's'
  return animal[0] === "s";
});
console.log(startsWithS);
console.log("\n")

/***************************  reduce() *******************************************/
var numbers = [10, 10, 10, 10];

// 1st way
var accumulateSum = numbers.reduce(function(accumulator, currentValue){
    console.log('The value of accumulator: ', accumulator);
    console.log('The value of currentValue: ', currentValue);
    return accumulator+currentValue;
  });
  console.log(accumulateSum);

// 2nd way with arrow function
var accumulateSum = numbers.reduce((accumulator, currentValue)=>{
  console.log('The value of accumulator: ', accumulator);
  console.log('The value of currentValue: ', currentValue);
  return accumulator+currentValue;
});
console.log(accumulateSum);


/***************************  map() *******************************************/
/* map -> returns a modified array */
var cats = ["Zelda", "Rumble", "Sam", "Flora"];
cats.map(catName => catName.toUpperCase()); //=> ["ZELDA", "RUMBLE", "SAM", "FLORA"]

/***************************  map() & filter() *******************************************/
var numbers = [2,4,6,5,7,9];
// map returns: [10,20,30,25,35,45], the filter() filters those and returns only the odd numbers:
console.log(numbers.map(number=>number*5).filter(number=> number %2 ==1));

/***************************************************** Operators ********************************************************************************************/

/***************************  spread operators *******************************************/
// arrays
let animals1= ["cat", "dog" , "rabbits"];
let animals2 = ["lion", "wolf", "leopard", "tiger"];
// using spread operator to print all animals into a single array:

let allAnimals = [...animals1, ...animals2];
console.log(allAnimals); //["cat", "dog" , "rabbits", "lion", "wolf", "leopard", "tiger"]

/***************************  spread operators *******************************************/
// objects
let name = {firstName:"Peter", lastName:"Oboro"};
let hobbies = { hobby1: "running", hobby2: "piano" }
let myInfo = {...name, ...hobbies};
// using spread operator to 'merge' the two objects into a sigle object
console.log(myInfo); //{firstName:"Peter", lastName:"Oboro", hobby1: "running", hobby2: "piano"}
