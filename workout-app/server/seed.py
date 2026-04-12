

from app import app
from models import *
from datetime import date

with app.app_context():

    
    print("Clearing old data...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()
    db.session.commit()

    
    print("Seeding exercises...")
    bench_press = Exercise(name="Bench Press", category="strength", equipment_needed=True)
    squat = Exercise(name="Squat", category="strength", equipment_needed=True)
    deadlift = Exercise(name="Deadlift", category="strength", equipment_needed=True)
    running = Exercise(name="Running", category="cardio", equipment_needed=False)
    cycling = Exercise(name="Cycling", category="cardio", equipment_needed=True)
    yoga = Exercise(name="Yoga Flow", category="flexibility", equipment_needed=False)

    db.session.add_all([bench_press, squat, deadlift, running, cycling, yoga])
    db.session.commit()

    
    print("Seeding workouts...")
    push_day = Workout(date=date(2024, 1, 15), duration_minutes=60, notes="Focus on chest and shoulders")
    leg_day = Workout(date=date(2024, 1, 17), duration_minutes=75, notes="Heavy leg day")
    cardio_day = Workout(date=date(2024, 1, 19), duration_minutes=45, notes="Active recovery cardio")

    db.session.add_all([push_day, leg_day, cardio_day])
    db.session.commit()

    
    print("Seeding workout exercises...")
    db.session.add_all([
        WorkoutExercise(workout_id=push_day.id, exercise_id=bench_press.id, sets=4, reps=10),
        WorkoutExercise(workout_id=push_day.id, exercise_id=yoga.id, sets=1, duration_seconds=600),
        WorkoutExercise(workout_id=leg_day.id, exercise_id=squat.id, sets=4, reps=8),
        WorkoutExercise(workout_id=leg_day.id, exercise_id=deadlift.id, sets=3, reps=6),
        WorkoutExercise(workout_id=cardio_day.id, exercise_id=running.id, sets=1, duration_seconds=1800),
        WorkoutExercise(workout_id=cardio_day.id, exercise_id=cycling.id, sets=1, duration_seconds=2400),
    ])
    db.session.commit()

    print("Done seeding!")