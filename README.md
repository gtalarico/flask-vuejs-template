# Flask-VueJs-Template

[![Build Status](https://travis-ci.org/gtalarico/flask-vuejs-template.svg?branch=master)](https://travis-ci.org/gtalarico/flask-vuejs-template)
[![codecov](https://codecov.io/gh/gtalarico/flask-vuejs-template/branch/master/graph/badge.svg)](https://codecov.io/gh/gtalarico/flask-vuejs-template)

_Flask + Vue.js Web Application Template_

![Vue Logo](/docs/vue-logo.png "Vue Logo") ![Flask Logo](/docs/flask-logo.png "Flask Logo")

[Live Demo](https://flask-vuejs-template.herokuapp.com/#/api)

## Features
* Minimal Flask App with modular Config
* [Flask-RestPlus](http://flask-restplus.readthedocs.io) API with class-based secure resource routing
* Starter [PyTest](http://pytest.org) test suite
* [vue-cli 3](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md) with Babel and ESlint.
* [Vuex](https://vuex.vuejs.org/) for state management
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://vuex.vuejs.org/) for backend communication
* Sample Vue [Filters](https://vuejs.org/v2/guide/filters.html)
* Heroku Configuration with one-click deployment

## Template Structure

The template uses Flask & Flask-RestPlus to create a REST style API,
and let's VueJs + vue-cli handle the front end and asset pipline.

### Blueprints

The Flask application is setup with with two blueprints:


#### Api Blueprint

Uses Flask-RestPlus to serve resources at the `/api` endpoint.
Flask-RestPlus can be discarded if you prefer standard view functions routing.

#### Client Blueprint

A simple Flask view is used to serve the entry point into the Vue application at the root endpoint `/`
The template uses vue-cli 3 and assumes Vue.js & Webpack will manage front-end resources and assets,
so it does overwrite template delimiter.

The Vue instance is preconfigured with Filters, Vue-Router, Vuex; each of these can easilly removed if they are not desired.

## Installation

##### Before you start

* Make sure node + npm are installed (tested with npm v5.6)
* Python 3 is installed (tested with 3.6)

##### Template and Dependencies

* Clone this repository:

	```
	$ git clone https://github.com/gtalarico/flask-vuejs-template.git
	```

* Create a [virtual enviroment](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies) (highly recommended)

* Install Python dependencies using pip or pipenv from the project directory:

	`$ pipenv install` or `pip install -r requirements.txt`

* Install npm dependencies

	```
	$ cd app/client/vue_app
	$ npm install
	```


## Development Server

While it's possible to use Flask to serve the vue app and the rest api, it is less than ideal as each change in client code would required a full rebuild and reload. Instead, we will use flask the serve the api endpoints, but we will serve the client app using the vue-cli dev server.
This combination allows you have both your backend python files and the Vue appplication files auto-reload on save.

This template also includes a few functions to help us manage the 2 servers.

This enables us to take advantage of Hot Module Replacement (HMR) and ESlint.
I think it is a small price to pay for the amount of time saved by HMR alone.

##### Api Server

From the root directory run:

```
$ python -m app serve_api
```

This will start the flask development server on `localhost:5000` and will respond to all requests on `/api.`.
This command is the same as running `python run.py`

##### Client Server

Start another terminal window, and from the same directory run:

```
$ python -m app serve_client
```

This will launch your browser and server the Vue application on `localhost:8080`. T
he vue app will hit `localhost:5000` to fetch resources.

This combination allows you have both your backend python files, as well as the Vue app files autoreload on each file save.


## Production Server

The production server uses Gunicorn to serve the entire application.
This template is configured to work with Heroku out of the box - just make sure you run `npm run build` before pushing it to your Heroku repository.

* Build your Vue Application:
```
$ python -m app build
```
This commands is a shorcut for cd-ing into `/app/client/vue_app` and running `$ npm run build`.

* Commit your code

* Setup your heroku app:

	```
	$ heroku apps:create flask-vuejs-template
	$ heroku config:set FLASK_CONFIG=Production
	$ heroku config:set SECRET=SECRETKEY
	$ heroku git:remote --app flask-vuejs-template
	```
* Push your application to heroku:

	```$ git push heroku```

### Heroku deployment - One Click Deploy

You can spin up your on version of this template on Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/gtalarico/flask-vuejs-template)
