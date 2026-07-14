import sqlite3
import os

DB_FOLDER = "data"
DB_NAME = "jhs.db"

os.makedirs(DB_FOLDER, exist_ok=True)

DB_PATH = os.path.join(DB_FOLDER, DB_NAME)


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_database():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS exercises(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        workout TEXT,
        exercise TEXT,
        muscle TEXT,
        rep_min INTEGER,
        rep_max INTEGER,
        rest INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS workout_sessions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        workout TEXT,
        date TEXT,
        duration INTEGER,
        notes TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS workout_sets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER,
        exercise TEXT,
        set_number INTEGER,
        weight REAL,
        reps INTEGER,
        rir REAL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bodyweight(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        weight REAL
    )
    """)

    conn.commit()

    load_exercises(conn)

    conn.close()


def load_exercises(conn):

    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM exercises")

    count = cur.fetchone()[0]

    if count > 0:
        return

    exercises = [

        ("A","Goblet Squat","Quads",8,10,180),
        ("A","DB Bench Press","Chest",8,12,150),
        ("A","Cable Row","Back",10,12,120),
        ("A","DB Romanian Deadlift","Hamstrings",10,12,150),
        ("A","DB Lateral Raise","Shoulders",12,15,90),
        ("A","Cable Pushdown","Triceps",12,15,90),
        ("A","Cable Crunch","Abs",15,20,60),

        ("B","Bulgarian Split Squat","Quads",10,12,180),
        ("B","Incline DB Press","Chest",8,12,150),
        ("B","Lat Pulldown","Back",10,12,120),
        ("B","DB Shoulder Press","Shoulders",8,12,120),
        ("B","Face Pull","Rear Delts",12,15,90),
        ("B","Incline Curl","Biceps",10,12,90),
        ("B","Standing Calf Raise","Calves",12,15,90),

        ("C","Leg Press","Quads",10,12,180),
        ("C","Chest Supported DB Row","Back",10,12,120),
        ("C","Cable Fly","Chest",12,15,90),
        ("C","DB Romanian Deadlift","Hamstrings",8,10,150),
        ("C","DB Lateral Raise","Shoulders",12,15,90),
        ("C","Overhead Rope Extension","Triceps",10,12,90),
        ("C","Hanging Knee Raise","Abs",12,15,60),

        ("D","Walking Lunge","Quads",10,12,120),
        ("D","Neutral Grip Pulldown","Back",10,12,120),
        ("D","Flat DB Bench Press","Chest",8,10,150),
        ("D","DB Shoulder Press","Shoulders",10,12,120),
        ("D","Rear Delt Fly","Rear Delts",12,15,90),
        ("D","Hammer Curl","Biceps",10,12,90),
        ("D","Seated Calf Raise","Calves",15,20,90)

    ]

    cur.executemany("""
        INSERT INTO exercises
        (workout,exercise,muscle,rep_min,rep_max,rest)
        VALUES (?,?,?,?,?,?)
    """, exercises)

    conn.commit()
