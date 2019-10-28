[![Build Status](https://travis-ci.org/arthurarty/fastfood-flask.svg?branch=dev)](https://travis-ci.org/arthurarty/fastfood-flask)
[![Maintainability](https://api.codeclimate.com/v1/badges/4147643247a2f57fcc5c/maintainability)](https://codeclimate.com/github/arthurarty/fastfood-flask/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/arthurarty/fastfood-flask/badge.svg?branch=dev)](https://coveralls.io/github/arthurarty/fastfood-flask?branch=dev)

# fastfood-flask
A proper flask implementation of fast food fast using flask.

#### how to run application.
Run the following docker commands.
```
- docker-compose build
- docker-compose up -d
```
Access database via the shell
```
- docker exec -it <db-container-name> psql -U postgres
- Create database called fastfood.
- docker exec -it <app-container-name> python manage.py db init
- docker exec -it <app-container-name> python manage.py db migrate
- docker exec -it <app-container-name> python manage.py db upgrade
```

Run tests
```
docker exec -it <app-container-name> pytest
docker exec -it <app-container-name> tox
```

Tests with converage
```
docker exec -it <app-container-name> coverage run -m pytest -v
docker exec -it <app-container-name> coverage report
```

Stop application
```
docker-compose stop
```

## Built With

* `FLask` : [Flask](http://flask.pocoo.org/) is a micro web framework written in Python.
* `SQL Alchemey` : [SQL Alchemey](https://www.sqlalchemy.org/) is an open-source SQL toolkit and object-relational mapper for the Python.
* `Docker` : [Docker](https://www.docker.com/) is a set of platform-as-a-service products that use OS-level virtualization to deliver software in packages called containers.
* `Travis`: [Travis CI](https://travis-ci.org/) is hosted continuous integration service used to build and test software projects hosted at GitHub.

## Authors

* **Nangai Arthur** - [Linkedin](www.linkedin.com/in/arthur-nangai)
