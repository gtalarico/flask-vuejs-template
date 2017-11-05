# Flask-Vue-Template

A project template for a Flask-Vue.js Web Application

### Background

I decided to put this together after spending some time trying to come up with a configuration that I like for a Flask-Vue integrated Application.

Unlike other templates I saw, this setup assumes you want to use Vue.js to manage all of your front-end resources and assets, and therefore,
it does not attempt to overwrite Jinja's or Vue's templating delimiter.

The Vue.js portion of the application is similar the official Vue.js Template "Webpack Simple" with a few minor tweaks (adds esline and friendly-errors).
It also adds minimal examples of basic usage of Filters, Mixins, Vue-Router for routing, Vuex for state management.

### Template Structure

The template is basically one Flask application with with two blueprints:

1. Api App: Blueprint uses FlaskRestful to serve resources at the `/api` url endpoint.
2. Client App: Minimal Blueprint used only to serve the a single-page Vue.js App  at the root endpoint `/`

### Development Server

For local development, I run both the Flask Development Server in parallel to webpack-dev-server.
This allows me to serve the Flask api endpoint, while still taking advantage of the hot-reload and eslint.

> From application root directory:

` python run.py`

This will server the `/api` endpoints at `localhost:5000`.
You could also server the JS application, but this would not handle hot-reloading, js linting, etc.

> from application/client/app:

`npm run dev`

This will server the Vue.js frontend application on `localhost:8080`.

Alternatively, you can also run just the flask server if you build your vuejs application first:

`npm run build`
This will pack the full application and save it in 'app/dist' where it can be served by the Flask Server.
The disadvantage of this method is that you have to wait for a full build after every change

### Production Server

The production server uses Gunicorn to serve the the Flask Application
[WIP]

### What's Included

#### Client App
* Vue.js
* Vuex
* Vue Router
* Bulma Css
* Axious
* es-lint
* friendly-errors-webpack-plugin
* Webpack loaders

#### Api App
* Flask
* FlaskRestful

# Heroku
`heroku apps:create flask-vuejs-template`
`heroku git:remote --app flask-vuejs-template`
`heroku config:set FLASK_CONFIG=Production`
`heroku config:set SECRET=SECRETKEY`
