"""
Jeremy's Hypertrophy System

Database Service Layer

Version: 1.1.0
"""

import sqlite3
import json

from pathlib import Path

from config import DATABASE_PATH, DATA_DIR


def get_connection():
    """
    Creates a database connection.
    """

    return sqlite3.connect(DATABASE_PATH)



def load_exercise_seed_data():
    """
    Loads exercise data from JSON file.
    """

    file_path = DATA_DIR / "seed_exercises.json"

    with open(file_path, "r") as file:
        return json.load(file)



def seed_exercises():
    """
    Inserts exercises into database.
    """

    exercises = load_exercise_seed_data()

    connection = get_connection()
    cursor = connection.cursor()


    for exercise in exercises:

        cursor.execute(
            """
            INSERT INTO exercises
            (
                workout,
                exercise_name,
                muscle_group,
                equipment,
                rep_min,
                rep_max,
                rest_time
            )

            VALUES (?, ?, ?, ?, ?, ?, ?)

            """,
            (
                exercise["workout"],
                exercise["exercise_name"],
                exercise["muscle_group"],
                exercise["equipment"],
                exercise["rep_min"],
                exercise["rep_max"],
                exercise["rest_time"],
            )
        )


    connection.commit()
    connection.close()



def get_exercises(workout):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM exercises
        WHERE workout = ?

        """,
        (workout,)
    )


    results = cursor.fetchall()

    connection.close()

    return results


if __name__ == "__main__":

    seed_exercises()

    print("Exercise library loaded successfully.")
