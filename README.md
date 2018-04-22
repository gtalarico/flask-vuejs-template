# Flask-VueJs-Template

_An all batteries included template for a Flask + Vue.js Web Application_


## Features
* Minimal Flask App with modular Config
* [Flask-RestPlus](http://flask-restplus.readthedocs.io) Api with class-based secure resourceful routing
* Starter [PyTest](http://pytest.org) test suite
* [Vue Cli 3 Template](https://github.com/vuejs-templates/webpack) with Babel, ESlint, and SASS loader.
* [Vuex](https://vuex.vuejs.org/) for state management
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://vuex.vuejs.org/) for backend communication
* Sample Vue Filters [Filters](https://vuejs.org/v2/guide/filters.html)
* Heroku Configuration with one-click deployment

## Template Structure

The template uses Flask + Flask RestPlus as a minimal REST Api and leaves the all front end work with Vue + Webpack.

The Flask application is setup with with two blueprints:


#### Api Blueprint

Uses FlaskRestful to serve restful resources at the `/api` url endpoint.
This blueprint users Flask RestPlus but it can be discarded if you prefer standard view functions routing.

#### Client Blueprint

Simple flask view is used to serve the entry point to the Vue application at the root endpoint `/`

This template assumes Vue.js and Webpack will manage front-end resources and assets so it does overwrite template delimiter.

The Vue application uses the official Vue Webpack template.

The main Vue instance is preconfigured with Filters, Mixins, Vue-Router, Vuex; each of these can easilly removed if they are not needed.



## Installation

##### Before you start
 
* Make sure node + npm are installed (tested with npm v5.6)
* Python 3 is installed

##### Setup Template and dependencies 

* Clone this repository
	`$ git clone https://github.com/gtalarico/flask-vuejs-template.git`

* Create a [virtual enviroment](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies) (highly recommended) 
* Install Python dependencies using pip or pipenv

	`$ pipenv install` or `pip install -r requirements.txt`

* Install npm dependencies
	
	`$ cd app/client/vue_App`

	`$ npm install`


### Development Server


From `app/client/vue_app`:

1. Build the VueJs Application:

	`$ npm run build`

2. From the application root directory:

	`$ python run.py`

This will server the `/api` endpoint _and_ the built Vue application at `localhost:5000`

The disadvantage of this method is that it does not offer hot-reloading, js linting, etc.

#### Development Server With HMD

There some advantages of running both the Flask Development Server in parallel to webpack-dev-server. It allows you to serve the Flask api endpoint while still taking advantage of the hot-reload and eslinter provided by webpack.

To take advantage of these features, keep the flask server running on `localhost:5000`, and then start the webpack dev server from another shell.

From `app/client/vue_app`:

`npm run serve`

This will server the Vue.js frontend application on `localhost:8080`.

Use `localhost:8080` during develoment to take advantage of hot-reloading and linting.

### Production Server

The production server uses Gunicorn to serve the entire application.
This template is configured to work with Heroku out of the box - just make sure you run `npm run build` before pushing it to your Heroku repository.


### Heroku deployment

```
$ heroku apps:create flask-vuejs-template
$ heroku git:remote --app flask-vuejs-template
$ heroku config:set FLASK_CONFIG=Production
$ heroku config:set SECRET=SECRETKEY
$ git push heroku
```

### Heroku deployment - One Click Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/gtalarico/flask-vuejs-template)
