/************** Objects **************/

let objectLiteral = {
    "first_key": "value_of_first_key",
    "second_key": "value_of_second_key"
    };
console.log(objectLiteral); 
const keysOfObject = Object.keys(objectLiteral); // the keys (property names) of the object literal
// objectLiteral["first_key"] or objectLiteral.first_key
console.log(`The first key is: ${keysOfObject[0]} and its value is: ${objectLiteral["first_key"]}`) // access the first key and value
console.log("\n")
/* In Python:

python_dict = {
    "first_key": "value_of_first_key",
    "second_key": "value_of_second_key"
}
print(python_dict)
# print the value if 1st key
list_of_keys = list(python_dict) # the keys (property names) of the object literal
print("The first key is: {} and its value is: {}".format(list_of_keys[0], python_dict["first_key"]))
*/


// delete a key
delete objectLiteral.second_key;
console.log(objectLiteral);
console.log("\n")

// Nested Objects
let nestedCarObjects = {
    "cars": {
        "production": ["mercedes", "bmw", "audi"],
        "year": [2020, 2018, 2016]
    },

    "motorbikes": "yamaha"
    };
console.log(nestedCarObjects.cars.production[0]); // mercedes
console.log("\n")


/*** Pass by reference ***/
// create a dicitonary
let carObj = {
    "production": "mercedes",
    "year": 2020
}
console.log("The original carObj was:\n");
console.log(carObj);
console.log("\n");

// create 2 example functions that can be used to alter the dictionary object
// this modifies the existing key-value pairs of carObj
let alterCarObj = obj => {
    obj["production"] = "bmw"
    obj.year = "2019"
};

// this introduces a new key-value pair
let addToCarObj = obj =>{
    obj["model"] = "random_model"
};

// call the functions with the carObj dictionary object in order to later apply the changes made
alterCarObj(carObj)
addToCarObj(carObj);
// print the modified dictionary object
console.log("The modified carObj now is:\n")
console.log(carObj);
console.log("\n");



/************* Methods **************/

let printText1 = "This first variable can be invoked from the object created below via the methods of the object 'objectPrintMessages'";
let printText2 = "This second variable can be invoked from the object created below via the methods of the object 'objectPrintMessages'";

let objectPrintMessages = {
    firstMessage(){
        console.log(printText1)
    }, 
    secondMessage(){
        console.log(printText2)
    },
    randomMessage(){
        console.log("This is a random message")
    }
};
// invoke the methods of the object objectPrintMessages
objectPrintMessages.firstMessage();
objectPrintMessages.secondMessage();
objectPrintMessages.randomMessage();
