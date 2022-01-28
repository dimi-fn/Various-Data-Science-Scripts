const menu = {
    _courses : {
        /* 3 properties: appetizers, mains, desserts */
        appetizers: [],
        mains: [],
        desserts: []
    },
    // create getter and setter methods for the properties above
    get appetizers(){
        return this._courses.appetizers;
    },
    get mains(){
        return this._courses.mains;
    },
    get desserts(){
        return this._courses.desserts;
    },
    set appetizers(appetizers){ // set appetizers(parameter), e.g. it could be set appetizers(data)
        this._courses.appetizers=appetizers;
    },
    set mains(mains){
        this._courses.mains = mains;
    },
    set desserts(desserts){
        this._courses(desserts) = desserts;
    },
    // getter for courses returning an object that contains key-value pairs for the properties
    get courses(){
        return {
            appetizers : this.appetizers,
            mains : this.mains,
            desserts : this.desserts
        };
    },
    // addDishToCourse() method creates a 'dish' object into the respective array in the menu's _courses object baded on the courseName
    addDishToCourse(courseName, dishName, dishPrice){
        const dish = {
            name: dishName,
            price: dishPrice
        };
        return this._courses[courseName].push(dish);
    },
    // getRandomDishFromCourse() method is applied inside the menu object having the courseName parameter
    getRandomDishFromCourse(courseName){
        // retrieve the array of the given course's dished from the menu's _courses object and store it to 'dishes'
        const dishes = this._courses[courseName];
        // generate a random index by multiplying Math.random() by the length of the dishes array
        // this guarantees that the random number will be between 0 and the length of the array. Math.floor() to turn it into a whole number
        // then return the dish located at that index
        const randomIndex = Math.floor(Math.random() * dishes.length);
        return dishes[randomIndex];
    },
    generateRandomMeal(){
        const appetizer = this.getRandomDishFromCourse("appetizers");
        const main = this.getRandomDishFromCourse("mains");
        const dessert = this.getRandomDishFromCourse("desserts");
        const totalPrice = appetizer.price + main.price + dessert.price;
        return `Your meal is ${appetizer.name}, ${main.name}, and ${dessert.name}, and the total price is ${totalPrice}`;
    }
};

menu.addDishToCourse("appetizers", "salad", 5);
menu.addDishToCourse("appetizers", "wings", 6);
menu.addDishToCourse("appetizers", "fries", 7.50);

menu.addDishToCourse("mains", "stake", 15);
menu.addDishToCourse("mains", "chicken", 13);
menu.addDishToCourse("mains", "salmon", 16.5);

menu.addDishToCourse("desserts", "ice cream", 3.5);
menu.addDishToCourse("desserts", "coffee", 3);
menu.addDishToCourse("desserts", "cake", 4);

const meal = menu.generateRandomMeal();
console.log(meal);