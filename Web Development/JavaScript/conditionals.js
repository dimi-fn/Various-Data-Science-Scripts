// Conditionals: if - else
if (false) {
    console.log('The code in this block will not run.');
  } else {
    console.log('But the code in this block will!');
  }

  let isNightTime = true;
  if (isNightTime) {
    console.log('Turn on the lights!');
  } else {
    console.log('Turn off the lights!');
  }
// the above code is equal with the below one by using ternary operator
isNightTime ? console.log('Turn on the lights!') : console.log('Turn off the lights!');

// switch 
let athleteFinalPosition = 'first place';

switch(athleteFinalPosition){
  case 'first place':
    console.log('You get the gold medal!');
    break;
  case 'second place':
    console.log('You get the silver medal!');
    break;
  case 'third place':
    console.log('You get the bronze medal!');
    break;
  default: // it is like else:
    console.log('No medal awarded.');
    break;
}

// if - else if - else
if (athleteFinalPosition=="first place"){
  console.log('You get the gold medal!');
} else if (athleteFinalPosition == 'second place'){
  console.log('You get the silver medal!');
} else if (athleteFinalPosition == 'third place'){
  console.log('You get the bronze medal!');
}
else {
  console.log("No medal awarded");
}
/* In Python:
if athleteFinalPosition == "first place":
  print("You get the gold medal")
elif athleteFinalPosition =="second place":
  print("You get the silver place")
elif athleteFinalPosition == "third place":
  print("You get the bronze medal")
else:
  print("No medal awarded")
*/
