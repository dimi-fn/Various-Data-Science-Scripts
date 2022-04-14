# Deployment

Contents
===============
* [Server](#server)
* [Client](#client)
    * [React](#react)
* [Webpack Setup with React](#webpack-setup-with-react)
* [Useful Sources](#useful-sources)


------------

# Server

Deploy the backend of your express app with Heroku:

* navigate inside the server directory and add a `Procfile`
    * inside the Procfile add this code required for Heroku: `web: npm start`, commit and push
    * make sure you configured your server like this: `const port = process.env.PORT || 3000;`
* Heroku
    * Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli)
    * via cmd, navigate in the root of your project
        * login to heroku via: `heroku login`
        * at your [Heroku dashboard](https://dashboard.heroku.com/apps) create a new app
        * now via your cmd again, run: `heroku git:remote -a <project-name>` where "project-name" is the app name given at heroku dashboard
        * push your server to heroku: `git subtree push --prefix server heroku master` ("subtree" because you are in the root and not inside the server path)
            * (if changes are made in the back-end of your github repo in the future, then in order to update heroku run the commands above from the beginning (apart from creating the app since it already exists))
* change all your fetch requests coming from your front-end at index.js (that request data on the back-end) by replacing `http://localhost:3000/<endpoint>` with `https://<heroku-app-name>.herokuapp.com/<endpoint>`
* you can make sure your backend works on heroku by checking one of your endpoints, e.g. `https://<heroku-app-name>.herokuapp.com/<endpoint>`

-------

# Client

Deploy your front-end at Netlify.

* On netlify, choose sites > add new site > import an existing project
    * search for your github repo and hit deploy
* On netlify, find "site settings" > "build & deploy" > "build settings" and make the following changes:
    * base directory: `client` (if client is the filename hosting your client)
    * publish directory: `client/` (if client is the filename hosting your client)
* On netlify: deployes > rigger deploy > deploy    
    * By default, auto publishing is on, hence, any change coming from your front-end repo will reflect on your netlify app as well
* Customize domain: site settings > domain management > domains > custom domains > options

## React

Deploying the client on Netlify if using React and Webpack (case where there is no server or database):

* package.json > scripts:
    * `"build": "webpack --config config/webpack.config.production.js"`

* Run `npm run build` to generate the *build* directory. Make sure it is located in the root project directory. Deploy that on GitHub

* If using a favicon:
    * put the favicon somewhere inside the *src*
    * at webpack.config.js: https://stackoverflow.com/questions/37298215/add-favicon-with-react-and-webpack 

* On Netlify
    * base directory: leave it 'not set'
    * publish directory: `/build`


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

* `npm install react react-dom react-router-dom`

----

* `npm run dev` to run the dev script     

### Testing with React

* [Testing with React](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Web%20Development/React#testing-react)

------

# Useful Sources

* https://dev.to/stlnick/how-to-deploy-a-full-stack-mern-app-with-heroku-netlify-ncb
