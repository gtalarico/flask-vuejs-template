# Flask-VueJs-Template 🌶️✌

[![Build Status](https://travis-ci.org/gtalarico/flask-vuejs-template.svg?branch=master)](https://travis-ci.org/gtalarico/flask-vuejs-template)
[![codecov](https://codecov.io/gh/gtalarico/flask-vuejs-template/branch/master/graph/badge.svg)](https://codecov.io/gh/gtalarico/flask-vuejs-template)

_Flask + Vue.js Web Application Template_

![Vue Logo](/docs/vue-logo.png "Vue Logo") ![Flask Logo](/docs/flask-logo.png "Flask Logo")

## Features
* Minimal Flask 1.0 App
* [Flask-RestPlus](http://flask-restplus.readthedocs.io) API with class-based secure resource routing
* Starter [PyTest](http://pytest.org) test suite
* [vue-cli 3](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md) + yarn
* [Vuex](https://vuex.vuejs.org/)
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://vuex.vuejs.org/) for backend communication
* Sample Vue [Filters](https://vuejs.org/v2/guide/filters.html)
* Heroku Configuration with one-click deployment + Gunicorn

## Demo
[Live Demo](https://flask-vuejs-template.herokuapp.com/#/api)

## Alternatives

If this setup is not what you are looking for, here are some similar projects:

* [oleg-agapov/flask-vue-spa](https://github.com/oleg-agapov/flask-vue-spa)
* [testdrivenio/flask-vue-crud](https://github.com/testdrivenio/flask-vue-crud)

#### Old Template

This template was updated to use a flatter folder structure and use yarn instead of npm.
You can now run `yarn serve` as well as other yarn commands from the template root directory.
The old template will be kept in the [npm-template branch](https://github.com/gtalarico/flask-vuejs-template/tree/npm-template) but will not be maintained. 

#### Django

Prefer Django? Checkout the [gtalarico/django-vue-template](https://github.com/gtalarico/django-vue-template)

## Template Structure

The template uses Flask & Flask-RestPlus to create a minimal REST style API,
and let's VueJs + vue-cli handle the front end and asset pipline.
Data from the python server to the Vue application is passed by making Ajax requests.

### Application Structure

#### Rest Api

The Api is served using a Flask blueprint at `/api/` using Flask RestPlus class-based
resource routing.

#### Client Application

A Flask view is used to serve the `index.html` as an entry point into the Vue app at the endpoint `/`.

The template uses vue-cli 3 and assumes Vue Cli & Webpack will manage front-end resources and assets, so it does overwrite template delimiter.

The Vue instance is preconfigured with Filters, Vue-Router, Vuex; each of these can easilly removed if they are not desired.

#### Important Files

| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/app`               | Flask Application                          |
| `/app/api`           | Flask Rest Api (`/api`)                    |
| `/app/client.py`     | Flask Client (`/`)                         |
| `/src`               | Vue App .                                  |
| `/src/main.js`       | JS Application Entry Point                 |
| `/public/index.html` | Html Application Entry Point (`/`)         |
| `/public/static`     | Static Assets                              |
| `/dist/`             | Bundled Assets Output (generated at `yarn build` |


## Installation

##### Before you start

Before getting started, you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install#mac-stable)
- [X] Vue Cli 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3
- [X] Pipenv (optional)
- [X] Heroku Cli (if deploying to Heroku)

##### Template and Dependencies

* Clone this repository:

	```
	$ git clone https://github.com/gtalarico/flask-vuejs-template.git
	```

* Setup virtual environment, install dependencies, and activate it:

	```
	$ pipenv install --dev
	$ pipenv shell
	```

* Install JS dependencies

	```
	$ yarn install
	```


## Development Server

Run Flask Api development server:

```
$ python run.py
```

From another tab in the same directory, start the webpack dev server:

```
$ yarn serve
```

The Vuejs application will be served from `localhost:8080` and the Flask Api
and static files will be served from `localhost:5000`.

The dual dev-server setup allows you to take advantage of
webpack's development server with hot module replacement.

Proxy config in `vue.config.js` is used to route the requests
back to Flask's Api on port 5000.

If you would rather run a single dev server, you can run Flask's
development server only on `:5000`, but you have to build build the Vue app first
and the page will not reload on changes.

```
$ yarn build
$ python run.py
```


## Production Server

This template is configured to work with Heroku + Gunicorn and it's pre-configured
to have Heroku build the application before releasing it.

#### JS Build Process

Heroku's nodejs buidlpack will handle install for all the dependencies from the `packages.json` file.
It will then trigger the `postinstall` command which calls `yarn build`.
This will create the bundled `dist` folder which will be served by whitenoise.

#### Python Build Process

The python buildpack will detect the `Pipfile` and install all the python dependencies.

#### Production Sever Setup

Here are the commands we need to run to get things setup on the Heroku side:

	```
	$ heroku apps:create flask-vuejs-template-demo
	$ heroku git:remote --app flask-vuejs-template-demo
	$ heroku buildpacks:add --index 1 heroku/nodejs
	$ heroku buildpacks:add --index 2 heroku/python
	$ heroku config:set FLASK_ENV=production
	$ heroku config:set FLASK_SECRET=SuperSecretKey

	$ git push heroku
	```

### Heroku deployment - One Click Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/gtalarico/flask-vuejs-template)
