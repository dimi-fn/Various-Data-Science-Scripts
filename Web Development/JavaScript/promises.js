/*
There are 3 states of the Promise object:
* Pending: by default, this is the Initial State, before the Promise succeeds or fails.
* Resolved: Completed Promise
* Rejected: Failed Promise
*/

/*
Promises syntax:

const promise = new Promise((resolve, reject) => {  
    let condition;
    
    if(condition is met) {    
        resolve('Promise is resolved successfully.');  
    } else {    
        reject('Promise is rejected');  
    }
});
*/

function addName (time, name){
    return new Promise ((resolve, reject) => {
      if(name){
        setTimeout(()=>{
          console.log(name)
          resolve();
        },time)
      }else{
        reject('No such name');
      }
    })
  }
  
  addName(2000, 'Joel')
    .then(()=>addName(2000, 'Victoria'))
    .then(()=>addName(2000, 'Peter'))
    .then(()=>addName(2000, 'Alex'))
    .then(()=>addName(2000, 'Sarah'))
    .catch((err)=>console.log(err))
