/* Functions */

function printHi(){
    console.log("Hi")
}
printHi();
console.log("\n");
/* In Python it would be:
def printHi():
    return("Hi")
printHi()  
*/

function rectangleArea(width, height) {
    if (width < 0 || height < 0) {
      return 'You need positive integers to calculate area!';
    }
    return width * height;
  }
console.log(rectangleArea(5,-1));
console.log("\n");
/* In Python:
def rectangleArea(width, height):
  if width<0 or height<0:
    return 'You need positive integers to calculate area!'
  return width*height
print(rectangleArea(5,-1))  
*/

// you can also assign the function's result into a variable:
var result = rectangleArea(5,-1);
console.log(result);

/******************* Helper Functions ~ function declarations *******************/
function multiplyByNineFifths(number) {
    return number * (9/5);
    };
    
function getFahrenheit(celsius) {
return multiplyByNineFifths(celsius) + 32;
};
console.log(getFahrenheit(15)); // Returns 59
console.log("\n");

/******************* Function Expressions *******************/
const isWeekend = function(day){
  if (day==="Saturday" || day==="Sunday"){
    return "Yea! It is " + day + ", so it is weekend!";
    } else {
      return "It is a weekday because it is " + day;
    }
  };
isWeekend("Tuesday")
console.log(isWeekend('Tuesday'));
isWeekend("Sunday")
console.log(isWeekend('Sunday'));
console.log("\n");

/******************* Arrow Functions *******************/
// without arrow function:
function rectangle_area(width, height){
  let area=width*height;
  return area;
}
rect_area = rectangle_area(5,3);
console.log(rect_area);

// arrow function:
let rectangle_area_arrow = (width, height) => {
  let rect_area = width * height;
  return rect_area;
};
console.log(rectangle_area_arrow(5,3));
