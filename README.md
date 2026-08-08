Workout App Backend

A backend REST API for a workout-tracking application built with Python, Flask, and SQLAlchemy.

The API allows personal trainers to create and manage workouts, add exercises, and associate exercises with specific workouts.

Technologies

* Python
* Flask
* SQLAlchemy
* Flask-Migrate
* Pipenv

Features

* Create and retrieve workouts
* Delete workouts
* Create and retrieve exercises
* Delete exercises
* Associate exercises with specific workouts
* Relational database management
* Database migrations and seeding

Installation

1. Clone the repository

git clone git@github.com:Yasmine101-101/workout-tracker-api.git
cd workout-tracker-api

2. Install dependencies

pipenv install
pipenv shell

3. Navigate to the server directory

cd server

4. Set up the database

Initialize the database migration:

flask db init

Create the initial migration:

flask db migrate -m "initial migration"

Apply the migration:

flask db upgrade head

5. Seed the database

python seed.py

Running the Application

Start the Flask application:

python app.py

The API will be available at:

http://127.0.0.1:5555

API Endpoints

Workouts

Method	Endpoint	Description
GET	/workouts	Get all workouts
GET	/workouts/<id>	Get a specific workout
POST	/workouts	Create a workout
DELETE	/workouts/<id>	Delete a workout

Exercises

Method	Endpoint	Description
GET	/exercises	Get all exercises
GET	/exercises/<id>	Get a specific exercise
POST	/exercises	Create an exercise
DELETE	/exercises/<id>	Delete an exercise

Workout Exercises

Method	Endpoint	Description
POST	/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises	Add an exercise to a workout

Project Overview

This project demonstrates practical experience with:

* REST API development
* Flask application development
* SQLAlchemy and relational databases
* CRUD operations
* Database migrations
* Database seeding
* API endpoint design
