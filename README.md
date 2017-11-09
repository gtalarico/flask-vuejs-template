# Flask-Vue-Template

A project template for a Flask-Vue.js Web Application

Note: In progress - comments and ideas are welcome.

## Motivation

I have been using Flask for a while and I recently started using Vue.js
I want to continue using Python as a Backend, but wanted migrate all frontend to a JS framework.
This template is what I ended up with after testing a few different configurations Flask-Vue integrated Application.

## Application Structure

The template is basically one Flask application with two blueprints:

1. Api App: Blueprint uses Flask-RESTful to serve resources at the `/api` url endpoint.
2. Client App: Minimal Blueprint used only to serve the a single-page Vue.js App  at the root endpoint `/`


#### Vue.js Structure (Client App)

The Vue.js application is served by the Client App Blueprint.

This template assumes you want to use Vue.js to manage all of your front-end resources and assets, and therefore,
it does not attempt to overwrite Jinja's or Vue's templating delimiter, not does it use flask-assets.

The Vue.js portion of the application is built on top of the official Vue.js Template "Webpack Simple" with a few minor tweaks (adds esline and friendly-errors).

The Vue.js application is also scaffolded with examples of basic usage of Filters, Mixins, Vue-Router for routing, Vuex for state management.

#### Flask Api Structure (Api App)

The second blueprint is served by the Api App Blueprint.
This blueprint is setup using Flask-RESTful, but that can be discarded for those that prefer to use standard function view and routes.


## Installation

1. Clone Repository
2. `pip install -r requirements.txt`


### Running Application (Local Development server)

> Note: For local development, I run both the Flask Development Server in parallel to webpack-dev-server.
This allows me to serve the Flask api endpoint, while still taking advantage of the hot-reload and eslint.

> From application root directory:

`python run.py`

This will server the `/api` endpoints at `localhost:5000`.
You could also server the JS application, but this would not handle hot-reloading, js linting, etc.

> from app/client/app:

`npm install`

To install npm dependencies.

`npm run dev`

This will serve the Vue.js frontend application on `localhost:8080`.

Alternatively, you can also run just the flask serve if you build your vuejs application first:

`npm run build`

This will pack the full application and save it in 'app/dist' where it can be served by the Flask Server.
The disadvantage of this method is that you have to wait for a full build after every change


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
