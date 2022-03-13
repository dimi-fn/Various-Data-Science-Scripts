# Deployment

Contents
===============
* [Server](#server)
* [Client](#client)
* [Useful Sources](#useful-sources)


------------

# Server

Deploy the backend of your express app with Heroku:

* navigate inside the server directory and add a `Procfile`
    * inside the Procfile add this code required for Heroku: `web: node server.js`, commit and push
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
    * base directory: `client`
    * publish directory: `client/`
* On netlify: trigger deploy > deploy    
    * By default, auto publishing is on, hence, any change coming from your front-end repo will reflect on your netlify app as well
* Customize domain: site settings > domain management > domains > custom domains > options


-------

# Useful Sources

* https://dev.to/stlnick/how-to-deploy-a-full-stack-mern-app-with-heroku-netlify-ncb
