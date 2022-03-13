/*
* document.querySelector()

*/



/****************************************** id1 ******************************************/
// 1) target element
const div1 = document.getElementById("id1");

// 2) add event with a callback function
div1.addEventListener("click", clickDiv1);

// 3) The callback function (action)
function clickDiv1(){
    console.log("hi div1")
};


/****************************************** id2 ******************************************/
// 1) target element
const div2 = document.getElementById("id2");

// 2) add event with a callback function
div2.addEventListener("click", clickDiv2);

// 3) The callback function (action)
function clickDiv2(){
    console.log("hi div2")
};


/****************************************** id3 ******************************************/
// 1) target element
const div3 = document.getElementById("id3");

// 2) add event with a callback function
div3.addEventListener("click", clickDiv3);

// 3) The callback function (action)
function clickDiv3(){
    console.log("hi div3");
    div3.removeEventListener("click", clickDiv3);
};

/* 
type - selector - callback
here we have:
* type -> click
* selector -> section
* callback -> console.log(...)

*/
function addGlobalEventListener(type, selector, callback) {
    document.addEventListener(type, e => {
        if (e.target.matches(selector)) callback(e)
    })
};

addGlobalEventListener("click", "section", e => {
    console.log("hi addGlobalEventListener!")
})


/****************************************** innerText******************************************/

const div6 = document.getElementById("id6");
div6.addEventListener("click", replaceTextDiv6);
function replaceTextDiv6(){
    div6.innerText = "Text was replaced after clicking via 'innerText'"
    // about the same with .textContent
}

/****************************************** append******************************************/

const div7 = document.getElementById("id7");
div7.addEventListener("click", appendTextDiv7);
function appendTextDiv7(){
    text = " text to be appended"
    div7.append(text)
}

/****************************************** style******************************************/

const div8 = document.getElementById("id8");
div8.addEventListener("click", changeBackColor);
function changeBackColor(){
    div8.style.backgroundColor = "blue";
}


