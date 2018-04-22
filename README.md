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

Uses FlaskRestful to serve restful resources at the `/api` url endpoint.
Flask-RestPlus can be discarded if you prefer standard view functions routing.

#### Client Blueprint

Simple flask view is used to serve the entry point to the Vue application at the root endpoint `/`

This template assumes Vue.js and Webpack will manage front-end resources and assets so it does overwrite template delimiter.

The Vue application uses the official Vue Webpack template.

The main Vue instance is preconfigured with Filters, Mixins, Vue-Router, Vuex; each of these can easilly removed if they are not needed.



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

While it's possibl to use Flask to serve the vue app and the rest api, it would be less then ideal as each change in your client code would required a full rebuild. Instead, we will use flask the serve the api endpoints, but we will serve the client app using the vue-cli dev server.

This will allows us to take advantage of Hot Module reload and ESlint. This is a small price to pay for the amount of time saved by Hot Module Reload alone!

##### Api Server

From the root directory run:

```
$ python run.py
```

This will start the flask development server on `localhost:5000` and will respond to all requests on `/api.`.

##### Client Server

Start another terminal window, and from the directory run:

```
$ python run_client.py
```

This will launch your browser and server the Vue application on `localhost:8080`. The vue app will hit `localhost:5000` to fetch resources.

This combination allows you have both your backend python files, as well as the Vue app files auto-reload on save.


## Production Server

The production server will use Gunicorn to serve the entire application.
This template is configured to work with Heroku out of the box - just make sure you run `npm run build` before pushing it to your Heroku repository.

* from `/app/client/vue_app` run:

```
$ npm run build
```

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
