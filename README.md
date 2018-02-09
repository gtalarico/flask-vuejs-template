# Flask-Vue-Template

A project template for a Flask-Vue.js Web Application

Note: PRs, comments and suggestions are welcome.

## Motivation

I have been using Flask for a while and I recently started using Vue.js.
I wanted to continue using Python as a Backend while migrating all frontend logic to VueJs.

## Application Structure

The template is basically a Flask application with with two blueprints:

1. Api App: Blueprint uses FlaskRestful to serve resources at the `/api` url endpoint.
2. Client App: Minimal Blueprint used only to serve a single-page Vue.js App at the root endpoint `/`


#### Vue.js Structure (Client App)

The Vue.js application is served by the Client App Blueprint.

This template assumes you want to use VueJs to manage all of your front-end resources and assets,
so it does not attempt to overwrite Jinja's or Vue's template delimiter.

The Vue portion of the application is built on top of the official Vue template "Webpack Simple" with a few minor tweaks -
adds [eslinter](https://www.npmjs.com/package/eslinter) and [friendly-errors](https://www.npmjs.com/package/friendly-errors-webpack-plugin).

The Vue application is also scaffolded with Filters, Mixins, Vue-Router, Vuex for state management.

#### Flask Api Structure (Api App)

The second blueprint is served by the Api Blueprint.
This blueprint is setup using Flask Restul, but that can easily discarded if you prefer to use standard view functions and routes.


## Installation

1. Clone Repository
2. `pip install -r requirements.txt`


### Running Application (Local Development server)

> For local development, I run both the Flask Development Server in parallel to webpack-dev-server.
This allows me to serve the Flask api endpoint while still taking advantage of the hot-reload and eslinter.

From `app/client/app`:

1. Install npm dependencies.

`npm install`

2. Build the VueJs Application:

`npm run build`

Then from the application root directory:

`python run.py`

This will server the `/api` endpoint _and_ the built Vue application at `localhost:5000`
The disadvantage of this method is that it does not offer hot-reloading, js linting, etc.

To take advantage of these features, keep the flask server running on `localhost:5000`, and then start the webpack dev server from another shell.

From `app/client/app`:

`npm run dev`

This will server the Vue.js frontend application on `localhost:8080`.

Use this url during develoment to take advantage of hot-reloading and linting.

### Production Server

The production server uses Gunicorn to serve the the Flask Application.
This template works with Heroku out of the box. Just make sure you run `npm run build`
before pushing it to your Heroku repository.


### Heroku deployment

```
heroku apps:create flask-vuejs-template
heroku git:remote --app flask-vuejs-template
heroku config:set FLASK_CONFIG=Production
heroku config:set SECRET=SECRETKEY
git push heroku
```

## What's Included

#### Client App
* Vue.js
* Vuex
* Vue Router
* Bulma Css
* Axios
* es-lint
* friendly-errors-webpack-plugin
* Webpack loaders

#### Api App
* Flask
* FlaskRestful
