# Test Driven Development (TDD)

Contents
====================

* [Categories of TDD](#categories-of-tdd)
* [Unit Testing with Jest](#unit-testing-with-jest)
* [How to Generate the bundle.js File](#how-to-generate-the-bundlejs-file)
* [Server](#server)
* [Webpack Setup with React](#webpack-setup-with-react)


-------

TDD is the approach of writing tests with the purpose of passing them correctly before the main code is even written.
* [TDD by Agile Aliance](https://www.agilealliance.org/glossary/tdd/#q=~(infinite~false~filters~(postType~(~'page~'post~'aa_book~'aa_event_session~'aa_experience_report~'aa_glossary~'aa_research_paper~'aa_video)~tags~(~'tdd))~searchTerm~'~sort~false~sortDirection~'asc~page~1))

Tools & Frameworks:
* [Jest](https://jestjs.io/), [Mocha](https://mochajs.org/), [Tape](https://github.com/substack/tape), [Jasmine](https://jasmine.github.io/)

-------

# Categories of TDD

`Unit tests`: e.g. testing a function

`Service tests` (Integration tests, API tests): testing groups of unit tests

`UI tests` (System tests, behaviour tests): when the overall program is tested

-------

# Unit Testing with Jest

Coding files: https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Web%20Development/TDD/testing_function

Create your project folder. On git bash and by being under the project directory, run:

* `npm init -y` (or just `npm init`) to initialize the project package
    * this will generate a **package.json** file

* `npm install jest --save-dev`    
    * this will generate a **pagkage-lock.json** file and a **node_modules** directory
        * it is a good practice to put the **node_modules** directory to .gitignore

* make a `/test` directory. There, create your (spec.js) file to be tested (in this example **fizzbuzz.js**), and the file that will test it, in this case **fizzbuzz.test.js**. I.e., the former file has the form of `<filename.js>` and the latter `<filename.test.js>`
    * e.g. in this example, create a function called 'fizzbuzz' at the fizzbuzz.js file:
        * The fizzbuzz function receives a number as its argument
        * When the number is a multiple of 3 and 5, it returns (“FizzBuzz”)
        * When the number is a multiple of 3, it returns (“Fizz”)
        * When the number is a multiple of 5, it returns (“Buzz”)
        * When the number is not a multiple of 3 or 5, it returns the number itself
    * after the fizzbuzz function, you have to export that as a module:
        * `module.exports = {fizzbuzz}`
    * Now, at the fizzbuzz.test.js file you can import the function and then test it    

* In order to run the tests: navigate to the **package.json** file and mofify:

        "scripts": {
            "test": "jest --watch"
        }


In this way, Jest will automatically look for files with a **.test.js** extension and run as many as it finds.

* `npm run test` for testing

* In order to have a check on what percentage of your test coverage, modify again the **package.json** file:
    * (test coverage is the percent of the degree to which the source code of a program is executed when a particular test suite is run)

        "scripts": {
        "test": "jest --watch --silent",
        "coverage": "jest --coverage"
        }

* Finally, run `npm run coverage`
    * it is a good practice to put the **coverage** folder generated into the .gitignore file

-------

# How to Generate the bundle.js File

There are mainly two reasons you may want to bundle all your JS files into a `bundle.js` file:
* every separate JS file creates a unique HTTP request to the browser, therefore it's not a good idea to have multiple JS files doing that
* the require() function cannot be interpreted correctly by the browser without the suitable instructions generated in the bundle.js file
* even if you have only one JS file, then again it might be a good idea to extract a bundle.js file for that your JS can be interpreted correctly on the majority of browsers (in which ECMAScript is used, and bundle.js can transfer the required interoperability that the webpages require)

----

* Currently you have the index.js file in the head section of the index.html with `<script defer src='index.js'></script>` (or before the end of the body without 'defer')
* `npm init -y` (done previously for jest)
* `npm install jest --save-dev` (not required here, done previously for jest)
* update package.json - as done previously:

        "scripts": {
            "test": "jest --watch --silent",
            "coverage": "jest --coverage"
            }

* `npm install -D watchify concurrently`
* browserify is similar to watchify
* Update "sciprts" at package.json (the first two lines are already there if jest had been used):

        "scripts": {
            "test": "jest --watch --silent",
            "coverage": "jest --coverage",
            "dev": "concurrently \"watchify ./index.js -o bundle.js\" \"python -m http.server\""
        }

* `npm run dev` (on **client** directory only, server can run with 'npm start' and it does not require bundling to run)
    * this will generate the bundle.js file, do that even if there is only one js file
    * having the terminal open with "npm run dev", this will handle all changes (adding of files and/or modifications) of your JS files automatically
    * this will run anything after "dev", in this case it was: `"dev": "concurrently \"watchify ./index.js -o bundle.js\" \"python -m http.server\""`

* Update your index.html: replace index.js with bundle.js
    * in the head section of index.html: `<script defer src='index.js'></script>` (or without 'defer' in the bottom before the end of the body)

----------

# Server

Navigate to the server dir:

* `npm init -y` (for npm package initialization)
* `npm install express` 
* `npm install jest --save-dev`  (for testing)
* `npm install jest supertest --save-dev` (for testing apis with express.js)
* `npm install cors` (cors is a node.js package for providing a Connect/Express middleware that can be used to enable CORS with various options)
* `npm install nodemon --save-dev` (update changes when done from the server, so that you don't have to re-launch the server)   

* Update the package.json:

        "start": "node server.js",
        "test": "jest --watch --silent",
        "coverage": "jest --coverage",
        "dev": "nodemon index.js"

* `npm run start` (same as `npm start`)

* index.js is:

        const server = require("./server");
        server.listen(3000, () => console.log("Express Server starting on port 3000"));

 * `node index.js` to run the server
    * message: "Express Server starting on port 3000" should be displayed on terminal
    * it can be accessed via browser at localhost:3000

* to run tests on the server:
    * `npm run test`, `npm run coverage`


---------

# Webpack Setup with React

Reasons for bundling
* bundling many JS files, i.e. reducing the http requests on browsers
* handling more file types
* automate additional tasks
* generate helper filers

## Folder Structure

* `config` directory
    * webpack files
* `public`: contains publicly accessible files
    * index.html
* `src`: contains the source code of the app
    * JS files
* .babelrc     

## Webpack configuration

* `webpack.config.js`
* `webpack.config.dev.js`: extra info for dev environment
* `webpack.config.production.js`: give instructions to webpack to build a production ready application

## Installations for Webpack
* `npm init -y`
* `npm install webpack webpack-cli webpack-dev-server html-webpack-plugin --save-dev`
* Install loaders
    * `npm i -D babel-loader style-loader css-loader`
        * same as `npm install babel-loader style-loader css-loader --save-dev`
* install Babel        
    * `npm i -D @babel/core @babel/preset-env @babel/plugin-transform-runtime @babel/preset-react`
        * @babel/core: the core babel library
        * @babel/preset-env: in order to target specific environments
        * @babel/plugin-transform-runtime: handles regenerator runtime errors
        * @babel/preset-react: use it if creating an app that uses React

* At package.json:
  
        "scripts": {
            "dev": "webpack serve --mode development --config config/webpack.config.dev.js",
            "build": "webpack --config config/webpack.config.production.js"
        },

or if using webpack cli then:        

        "scripts": {
            "dev": "webpack-cli serve --mode development --config config/webpack.config.dev.js",
            "build": "webpack --config config/webpack.config.production.js"
        },


## Installations for React

* `npm install react react-dom`

----

* `npm run dev` to run the dev script     

## Testing with React

* [Testing with React]()
