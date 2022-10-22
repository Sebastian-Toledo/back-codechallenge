# Back

## Dependencies

- Python 3.10.8

- Django 4.1.0

## Instructions

- Clone repo

- cd to project folder

- install Python and Django

- python manage.py makemigration

- python manage.py migrate

- python manage.py createsuperuser

## How to use

- python manage.py runserver

- login [localhost:8000/admin]() with your super user and create user, friends and lessons

## Api endpoints

- `users/` List all users in the system
- `friendships/` List all friendships registered in the system
- `user/<str:username>` List of all friends for a specific user
- `lesson/<str:username>` List of lessons that a specific user has taken
- `external_api/pokemones` List of pokemons from pokeapi
