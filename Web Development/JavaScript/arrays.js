/***************** Arrarys *****************/
let car_array = ["mercedes", "bmw", "audi"];
console.log(`the array of cars is: ${car_array}`);
console.log(`the first car in array is: ${car_array[0]}`);
console.log(`There are ${car_array.length} cars in this array`); // Python: len(car_array) 

// .push(): add element to array
car_array.push("ferrari", "ford") // Python: car_array.extend(["ferrari", "ford"]), also .append() for adding 1 element
console.log(`the new array is now: ${car_array}`);

// .pop(): remove last element of an array (it doesn't take any arguments, it just removes the last item)
car_array.pop() // Python: car_array.pop(), del(car_array[-1])

// .slice()
console.log(`The 2nd and 3rd car in the array are: ${car_array.slice(1,3)}`); // Python: print(car_array[1:3])

//indices
console.log(`The index of mercedes car in the array is: ${car_array.indexOf("mercedes")}`); // Python: print(car_array.index("mercedes"))