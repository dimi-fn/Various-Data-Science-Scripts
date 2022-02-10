// given an array of primitive types, i.e. int, string, number, booleans and numbers
// Write a function diffTypes that will return an object (see example below)
// => { string: 1, array: 1, boolean: 2, object: 1, number: 1 }


function diffTypes(arr) {
    
    let count_strings =0;
    let count_numbers=0;
    let count_booleans=0;
    let count_arrays=0;
    let count_objects=0;

    for (i=0; i< arr.length; i++){
        if (typeof arr[i] == "string"){
            count_strings+=1; 
        } else if (typeof arr[i] == "number"){
            count_numbers+=1;
        } else if (typeof arr[i] == "boolean"){
            count_booleans+=1;
        } else if (Array.isArray(arr[i])){
            count_arrays+=1;
        }
        else if (typeof arr[i]== "object"){
            count_objects+=1;
        }
    };
    return {
        "string": count_strings,
        "array": count_arrays,
        "boolean": count_booleans,
        "object": count_objects,
        "number": count_numbers
    };

}

const ar = [
  1,
  "str",
  false,
  { name: 'Romeo', age: 77 },
  ["a", "e", "i", "o", "u"],
  true
]
console.log(diffTypes(ar))
// => { string: 1, array: 1, boolean: 2, object: 1, number: 1 }
