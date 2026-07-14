"""
Jeremy's Hypertrophy System
Database Initialization

Version: 1.1.0
"""

import sqlite3

from config import DATABASE_PATH, DATA_DIR


def create_database():

    DATA_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()


    # Exercises Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercises (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        workout TEXT NOT NULL,

        exercise_name TEXT NOT NULL,

        muscle_group TEXT,

        equipment TEXT,

        rep_min INTEGER,

        rep_max INTEGER,

        rest_time INTEGER

    )
    """)


    # Workout Templates

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workout_templates (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        workout_name TEXT UNIQUE NOT NULL

    )
    """)


    # Workout Exercise Relationships

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workout_exercises (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        workout_id INTEGER,

        exercise_id INTEGER,

        exercise_order INTEGER

    )
    """)


    # Completed Workouts

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workout_sessions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        date TEXT,

        workout TEXT,

        duration INTEGER,

        notes TEXT

    )
    """)


    # Individual Sets

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workout_sets (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        session_id INTEGER,

        exercise TEXT,

        set_number INTEGER,

        weight REAL,

        reps INTEGER,

        rir INTEGER

    )
    """)


    # PR Tracking

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personal_records (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        exercise TEXT,

        best_weight REAL,

        best_reps INTEGER,

        estimated_1rm REAL

    )
    """)


    # Body Weight

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS body_weight (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        date TEXT,

        weight REAL

    )
    """)


    # Application Settings

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        setting_name TEXT,

        setting_value TEXT

    )
    """)


    connection.commit()

    connection.close()


if __name__ == "__main__":

    create_database()

    print("JHS database created successfully.")