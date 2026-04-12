from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from marshmallow import ValidationError

from models import *
from schemas import (
    workout_schema, workouts_schema,
    exercise_schema, exercises_schema,
    workout_exercise_schema
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


# GET /workouts - list all workouts
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts)), 200


# GET /workouts/<id> - get one workout with its exercises
@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({'error': 'Workout not found'}), 404
    return jsonify(workout_schema.dump(workout)), 200


# POST /workouts - create a new workout
@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()
    try:
        validated = workout_schema.load(data)
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400

    try:
        workout = Workout(
            date=validated['date'],
            duration_minutes=validated['duration_minutes'],
            notes=validated.get('notes')
        )
        db.session.add(workout)
        db.session.commit()
        return jsonify(workout_schema.dump(workout)), 201
    except ValueError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# DELETE /workouts/<id> - delete a workout
@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({'error': 'Workout not found'}), 404
    db.session.delete(workout)
    db.session.commit()
    return jsonify({'message': 'Workout deleted'}), 200


# GET /exercises - list all exercises
@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises)), 200


# GET /exercises/<id> - get one exercise with its workouts
@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return jsonify({'error': 'Exercise not found'}), 404
    return jsonify(exercise_schema.dump(exercise)), 200


# POST /exercises - create a new exercise
@app.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()
    try:
        validated = exercise_schema.load(data)
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400

    try:
        exercise = Exercise(
            name=validated['name'],
            category=validated['category'],
            equipment_needed=validated['equipment_needed']
        )
        db.session.add(exercise)
        db.session.commit()
        return jsonify(exercise_schema.dump(exercise)), 201
    except ValueError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# DELETE /exercises/<id> - delete an exercise
@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return jsonify({'error': 'Exercise not found'}), 404
    db.session.delete(exercise)
    db.session.commit()
    return jsonify({'message': 'Exercise deleted'}), 200


# POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
# add an exercise to a workout
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def create_workout_exercise(workout_id, exercise_id):
    workout = Workout.query.get(workout_id)
    if not workout:
        return jsonify({'error': 'Workout not found'}), 404

    exercise = Exercise.query.get(exercise_id)
    if not exercise:
        return jsonify({'error': 'Exercise not found'}), 404

    data = request.get_json()
    try:
        validated = workout_exercise_schema.load(data)
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400

    try:
        workout_exercise = WorkoutExercise(
            workout_id=workout_id,
            exercise_id=exercise_id,
            reps=validated.get('reps'),
            sets=validated.get('sets'),
            duration_seconds=validated.get('duration_seconds')
        )
        db.session.add(workout_exercise)
        db.session.commit()
        return jsonify(workout_exercise_schema.dump(workout_exercise)), 201
    except ValueError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(port=5555, debug=True)