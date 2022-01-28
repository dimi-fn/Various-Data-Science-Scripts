const getUserChoice = userInput => {

    userInput = userInput.toLowerCase();
  
    if (userInput === "rock" || userInput === "paper" || userInput==="scissors" || userInput ==="bomb"){
      return userInput;
    } else{
      console.log("Error: Please type 'rock', 'paper' or 'scissors'!");
    };
  };
   
  
const getComputerChoice = () => {
    /*
    - returns a random number between 0 and 2 
    * Math.random() gives a random number betwen 0 and 1
    * but we want a number till 3, hence multiply that by 3
    * then floor it to ignore all floating number cases
    */
    const randomNumber =  Math.floor(Math.random() * 3);
    if (randomNumber === 0){
        return "rock"
    } else if (randomNumber === 1){
        return "paper";
    } else{
        return "scissors";
    };
}; 
// check
// console.log(getComputerChoice());


const determineWinner = (userChoice, computerChoice) => {
    if(userChoice === computerChoice){
        return "This game round is a tie!";
    }else if (userChoice==="rock"){
        if (computerChoice ==="paper"){
        return "Computer won!";
        }else{
        return "You won!";
        }
    }else if (userChoice==="paper"){
        if (computerChoice==="scissors"){
        return "Computer won!";
        }else{
        return "You won!";
        }
    }else if (userChoice==="scissors"){
        if (computerChoice === "rock"){
        return "Computer Won";
        }else{
        return "You won!"
        }
    }else if (userChoice==="bomb"){
        return "You won!";
    }
    };
/* check all combinations work fine
console.log(determineWinner("rock", "rock")); // This game round is a tie!
console.log(determineWinner("paper", "paper")); // This game round is a tie!
console.log(determineWinner("scissors", "scissors")); // This game round is a tie!

console.log(determineWinner("rock", "paper")); // Computer won!
console.log(determineWinner("rock", "scissors")); // You won!
console.log(determineWinner("paper", "rock")); // You won!
console.log(determineWinner("paper", "scissors")); // Computer won!
console.log(determineWinner("scissors", "rock")); // Computer won!
console.log(determineWinner("scissors", "paper")); // You won!

console.log(determineWinner("bomb", "paper")); // You won!
console.log(determineWinner("bomb", "rock")); // You won!
console.log(determineWinner("bomb", "scissors")); // You won!
*/

const playGame = () => {
    const userChoice = getUserChoice("rock");
    const computerChoice = getComputerChoice();
    console.log(`You threw ${userChoice}`);
    console.log(`The computer threw ${computerChoice}`);
    console.log(determineWinner(userChoice, computerChoice));
};
playGame();