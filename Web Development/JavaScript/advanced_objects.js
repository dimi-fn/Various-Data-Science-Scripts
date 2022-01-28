/* Advanced objects */

const carObject = {
    brand: "mercedes",
    model : "C class", 
    provideInfo(){
      /*
      If we do: 
      return `The brand of this car object is: ${brand}, and its model is: ${model}.`
      , i.e. without 'this' then we'll have the error --> ReferenceError: brand/model is not defined
      */  
      return `The brand of this car object is: ${this.brand}, and its model is: ${this.model}.`
    }
  };
  
  // check .provideInfo() has access to the internal properties of the carObject and print its value
  console.log(carObject.provideInfo());
  console.log("\n")



/***************************** Privacy on object properties *****************************/
// via the naming convention "_"

const robot = {
    // _energyLevel: property should not be altered
    _energyLevel: 100,
    recharge(){
      this._energyLevel += 30;
      console.log(`Recharged! Energy is currently at ${this._energyLevel}%.`)
    }
  };
  
// uncomment to see the difference
// although energyLevel has '_' it is still possible to reassign it with "._":
// robot._energyLevel = 200;

robot.recharge();
console.log("\n")



/***************************** Getters & Setters *****************************/
/* Getters */
const person = {
    _firstName: 'Peter',
    _lastName: 'Doe',
    get fullName() {
      if (this._firstName && this._lastName){
        return `${this._firstName} ${this._lastName}`;
      } else {
        return 'Missing a first name or a last name.';
      }
    }
  }
   
// Call the getter method: 
console.log(person.fullName); // 'Peter Doe'
console.log("\n")

// another example
const roboT = {
    _model: 'xxy',
    _energyLevel: 100,
    get energyLevel(){
        if(typeof this._energyLevel === 'number') {
            return 'The current energy level is ' + this._energyLevel
        } else {
            return "System malfunction: cannot retrieve energy level"
        }
    }
};
console.log(roboT.energyLevel);
  
  
/* Setters */
const personB = {
    _age: 37,
    set age(newAge){
      if (typeof newAge === 'number'){
        this._age = newAge;
      } else {
        console.log('You must assign a number to age');
      }
    }
  };

personB.age = 40; // personB._age = 40;
console.log(personB._age); // Logs: 40
personB.age = '40'; // Logs: You must assign a number to age  
console.log("\n")

// example of both a getter and a setter
// getter will grab the initial value of numOfSensors, setter will reassign it
const robotC = {
    _model: 'XXXYYY',
    _energyLevel: 100,
    _numOfSensors: 15,
    get numOfSensors(){
      if(typeof this._numOfSensors === 'number'){
        return this._numOfSensors;
      } else {
        return 'Sensors are currently down.'
      }
    },
    set numOfSensors(num) {
      if (typeof num === 'number' && num >= 0){
        this._numOfSensors = num;
      } else {
        console.log('Pass in a number that is greater than or equal to 0')
      }   
    } 
  };
  
  robotC.numOfSensors = 100;
  console.log(robotC.numOfSensors); // 100
  console.log("\n")
  
  

/***************************** Factory Functions *****************************/
const carFactory = (brand, model, year) => {
    // factory function with 3 parameters (brand, model, year) returning an object with 4 properties (brand, model, year, logCars())
return { 
    brand: brand,
    model: model, 
    year: year,
    logCars() {
    console.log(`This is a ${brand} ${model} produced in ${year}`);
    console.log("\n")
    } 
}
};

// call the newCar object as a result of calling carFactory with the needed arguments
const newCar = carFactory('mercedes', "C class", 2020) 
newCar.logCars(); // This is a mercedes C class produced in 2020
// Similary, we can invoke again the carFactory function to log multiple cars

/* property value shorthand */
// the same function above, but with the property value shorthand technique
const carFactory2 = (brand, model, year) => {
    // factory function with 3 parameters (brand, model, year) returning an object with 4 properties (brand, model, year, logCars())
return { 
    brand, 
    model,
    year,
    logCars() {
    console.log(`This is a ${brand} ${model} produced in ${year}, with property value shorthand`);
    console.log("\n")
    } 
}
};

// call the newCar object as a result of calling carFactory2 with the needed arguments
const newCar2 = carFactory2('mercedes', "C class", 2020) 
newCar2.logCars(); // This is a mercedes C class produced in 2020


/* Destructured Assignment */ 
const robot_destructive = {
    model: 'XXXYYY',
    energyLevel: 100,
    functionality: {
      beep() {
        console.log('Beep Boop');
      },
      fireLaser() {
        console.log('Pew Pew');
      },
    }
  };
  

// extract "energyLevel" in a classic way
const energy_level = robot_destructive.energyLevel;
console.log(energy_level);

// extract 'energyLevel' via Destructured Assignment technique
const {energyLevel} = robot_destructive; 
console.log(energyLevel);
