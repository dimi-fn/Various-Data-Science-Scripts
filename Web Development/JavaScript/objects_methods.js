/************** Objects **************/

let objectLiteral = {
    "first_key": "value_of_first_key",
    "second_key": "value_of_second_key"
    };
console.log(objectLiteral); 
const keysOfObject = Object.keys(objectLiteral); // the keys (property names) of the object literal
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



/************* Methods **************/

let printText1 = "This first variable can be invoked from the object created below via the methods of the object";
let printText2 = "This second variable can be invoked from the object created below via the methods of the object";

let objectPrintMessages = {
    firstMessage(){
        console.log(printText1)
    }, 
    secondMessage(){
        console.log(printText2)
    },
    randomMessage(){
        console.log("a random message")
    }
};
// invoke the methods of the object objectPrintMessages
objectPrintMessages.firstMessage();
objectPrintMessages.secondMessage();
objectPrintMessages.randomMessage();