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


/*** Privacy on object properties***/
// via the naming convention "_"