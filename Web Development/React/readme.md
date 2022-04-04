# React

Contents
===================
* [General](#general)
* [Components](#components)
* [State](#state)
* [Eventing](#eventing)



-------

# General

* [React doc](https://reactjs.org/)

* [JSX](https://reactjs.org/docs/introducing-jsx.html)
    * JSX stands for JavaScript XML. JSX allows us to write HTML in React.

* `DOM vs virtual DOM`
    * virtual DOM is like an abstraction of the DOM
    * with virtual DOM when you make a change then the DOM will re-charge only for the place that has some change, whereas with DOM all DOM will re-charge no matter the change

* [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)
    * you can look the components of page by choosing "components" in dev tools

-----

# Components

Components are independent and reusable bits of code
* ther are: class components and functional components
    * most common: functional components
* every component is a function and needs to be capitalized
* put all components in a directory inside a src folder
* components can be rendered inside of other components
* we can create variables and use the JSX to display the values.

<br>

* [Controlled Components](https://reactjs.org/docs/forms.html#controlled-components)

-----

# State

* `useState` hook
    * only functional components can use that
    * you must only use useState hook at the top level of the component (e.g. do not nest it within an if block). The same rationale applies for all hooks
* The useState hook returns an array with two elements
    * The 1st element is the value held in the current state
    * The 2nd is a function we can use to update that value
    
# Eventing    

Eventing: when the state gets updated as a reaction to an event (e.g. user's clicking a 'like' button and counting the total number of likes)
    * events: e.g. `onClick`, `onHover`, `onSubmit`
    * as with the 'regular' event handlers, we can have access to the event itself
