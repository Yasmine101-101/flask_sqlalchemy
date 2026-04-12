# flask_sqlalchemy
# Workout App Backend

## Description

This is a backend API for a workout tracking app. I built it using Flask and SQLAlchemy. It lets personal trainers create workouts, add exercises, and link exercises to specific workouts.

## Installation

1. Clone the repo:
```bash
git clone <your-repo-url>
cd workout-app
```

2. Install dependencies:
```bash
pipenv install
pipenv shell
```

3. Go into the server folder:
```bash
cd server
```

4. Set up the database:
```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade head
```

5. Seed the database:
```bash
python seed.py
```

## How to Run

```bash
python app.py
```

App runs on `http://127.0.0.1:5555`

## Endpoints

### Workouts
| Method | Endpoint | What it does |
|--------|----------|-------------|
| GET | /workouts | get all workouts |
| GET | /workouts/\<id\> | get one workout |
| POST | /workouts | create a workout |
| DELETE | /workouts/\<id\> | delete a workout |

### Exercises
| Method | Endpoint | What it does |
|--------|----------|-------------|
| GET | /exercises | get all exercises |
| GET | /exercises/\<id\> | get one exercise |
| POST | /exercises | create an exercise |
| DELETE | /exercises/\<id\> | delete an exercise |

### Workout Exercises
| Method | Endpoint | What it does |
|--------|----------|-------------|
| POST | /workouts/\<workout_id\>/exercises/\<exercise_id\>/workout_exercises | add an exercise to a workout |