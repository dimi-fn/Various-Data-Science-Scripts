/* Objects */

let objectLiteral = {
    "first_key": "value_of_first_key",
    "second_key": "value_of_second_key"
    };
console.log(objectLiteral); 
const keysOfObject = Object.keys(objectLiteral); // the keys (property names) of the object literal
console.log(`The first key is: ${keysOfObject[0]} and its value is: ${objectLiteral["first_key"]}`) // access the first key and value
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
delete objectLiteral.first_key;
