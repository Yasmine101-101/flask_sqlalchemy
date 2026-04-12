from marshmallow import Schema, fields, validate


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(dump_only=True)
    exercise_id = fields.Int(dump_only=True)
    reps = fields.Int(load_default=None)
    
    sets = fields.Int(load_default=None, validate=validate.Range(min=1, error="Sets must be at least 1"))
    duration_seconds = fields.Int(load_default=None)

    exercise = fields.Nested(lambda: ExerciseSchema(only=('id', 'name', 'category', 'equipment_needed')), dump_only=True)


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    
    duration_minutes = fields.Int(required=True, validate=validate.Range(min=1, error="Duration must be at least 1 minute"))
    notes = fields.Str(load_default=None)

    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema), dump_only=True)


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    
    name = fields.Str(required=True, validate=validate.Length(min=1, error="Name cannot be empty"))
    
    category = fields.Str(required=True, validate=validate.OneOf(
        ['strength', 'cardio', 'flexibility'],
        error="Category must be strength, cardio, or flexibility"
    ))
    equipment_needed = fields.Bool(required=True)

    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema), dump_only=True)



workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_exercise_schema = WorkoutExerciseSchema()