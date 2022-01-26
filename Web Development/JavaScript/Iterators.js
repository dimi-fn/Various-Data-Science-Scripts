/********** Iterators **********/

const cars = ["mercedes", "bmw", "audi", "ferrari"];

// Iterator: .forEach()
// 1st way
cars.forEach(function(carItem){
    console.log(`This is a ${carItem} car`);
});
console.log("\n")

// 2nd way with arrow function
cars.forEach(carItem => console.log(`This is a ${carItem} car`));

// Iterator: .map()
var carsUpper = cars.map(element => element.toUpperCase());
console.log(carsUpper);
console.log("\n")

// Iterator: filter
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

// .findIndex()
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

/********* .reduce() *********/

const numbers = [10, 10, 10, 10];

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
