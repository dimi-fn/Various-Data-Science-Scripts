# React

Contents
===================
* [General](#general)
* [Components](#components)
* [State](#state)
* [Eventing](#eventing)
* [Hooks](#hooks)
* [CSS with React](#css-with-react)
* [Testing React](#testing-react)



----------------

# General

* [React doc](https://reactjs.org/)
    * React uses a syntax extension of JavaScript called JSX (JavaScript XML) that allows you to write HTML directly within JavaScript.
    * because JSX is not valid JavaScript, JSX code must be compiled into JavaScript. The **Babel** transpiler is a popular tool for this process
    * nested JSX must return a single element

* [JSX](https://reactjs.org/docs/introducing-jsx.html)
    * JSX stands for JavaScript XML. JSX allows us to write HTML in React.

* `DOM vs virtual DOM`
    * virtual DOM is like an abstraction of the DOM
    * with virtual DOM when you make a change then the DOM will re-charge only for the place that has some change, whereas with DOM all DOM will re-charge no matter the change

* [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)
    * you can look the components of page by choosing "components" in dev tools

React is:
* `declarative`: we tell React what we want and it will figure out how to do it, i.e. it is not imperative

-----

# Components

Components are independent and reusable bits of code
* they can be consisted of: **class** components and **functional** components
    * most common: functional components
* every component is a function and needs to be capitalized
* put all components in a directory inside a src folder
* components can be rendered inside of other components
* we can create variables and use JSX to display the values.
* you cannot use hooks in class components - [instead use React Lifecycle Methods](https://www.codecademy.com/learn/react-101/modules/react-102-lifecycle-methods-u/cheatsheet)

<br>

* [Controlled Components](https://reactjs.org/docs/forms.html#controlled-components)

-----

# State

React functional components can save local state data via the `useState` hook

* `useState` hook
    * only functional components can use that
    * you must only use useState hook at the top level of the component (e.g. do not nest it within an if block statement). The same rationale applies for all hooks
* The useState hook returns an array with two elements:
    * The 1st element is the value held in the current state
    * The 2nd is a function we can use to update that value 
        * something like [getter, setter], e.g. [getUsername, setUsername]
* useState can be used multiple times to get more than one *state*  

<br>    

* [React Reconciliation](https://reactjs.org/docs/reconciliation.html)

# Eventing    

Eventing: when the state gets updated as a reaction to an event (e.g. user's clicking a 'like' button and counting the total number of likes)
    * events: e.g. `onClick`, `onHover`, `onSubmit`
    * as with the 'regular' event handlers, we can have access to the event itself


<br>

* [SyntheticEvent](https://reactjs.org/docs/events.html)

--------

# Hooks

Rules about hooks:
* they start with '`Use`'
* they are functions (cannot be used as class components)
* hooks should not be inside conditions, e.g. inside if statements of various states
    * because there might be a mismatch between states and then that hook will not be able to work


-----------------

# CSS with React

* [Styling & CSS](https://reactjs.org/docs/faq-styling.html)
* [React Bootstrap](https://react-bootstrap.github.io/)


---------

# Testing React

* Install the required dependencies:

        npm install --save-dev jest babel-jest @testing-library/react @testing-library/jest-dom @testing-library/user-event

* In package.json, add Jest configurations to handle various static assets like CSS and other file types


        "jest": {
            "moduleNameMapper": {
            "\\.(jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2|mp4|webm|wav|mp3|m4a|aac|oga)$": "<rootDir>/__mocks__/fileMock.js",
            "\\.(css|less)$": "<rootDir>/__mocks__/styleMock.js"
            }, // might also need to add the following:
            "testEnvironment": "jsdom"

* In package.json also add the value for "test" and coverage (for npm run coverage)


        "test": "jest --watch --setupFilesAfterEnv ./src/test/setupTests.js",
        "coverage": "jest --setupFilesAfterEnv ./src/test/setupTests.js --coverage --watchAll=false"

* Create a folder called `__mocks__ ` with a `fileMock.js` and a `styleMock.js` file
