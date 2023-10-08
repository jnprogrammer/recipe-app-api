# recipe-app-api
Recipe api project - Django TDD 

Linting

 docker-compose run --rm app sh -c "flake8"

 Getting django project setup with in container

 docker-compose run --rm app sh -c "django-admin startproject app ."

testing github actions on push

This project uses Docker-compose to develope the project in a clean enviroment with pre-selected tools at particular versions. 

"make a django admin"
docker-compose run --rm app sh -c "python manage.py createsuperuser"