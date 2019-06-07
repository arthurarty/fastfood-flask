[![Build Status](https://travis-ci.org/arthurarty/fastfood-flask.svg?branch=dev)](https://travis-ci.org/arthurarty/fastfood-flask)

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
docker exec -it <app-container-name> converage html
```