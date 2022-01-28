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


/*** Privacy on object properties***/
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
// although energyLevel has '_' it is still possible to reassign it:
// robot._energyLevel = 200;

robot.recharge();