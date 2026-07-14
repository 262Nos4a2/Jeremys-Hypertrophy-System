"""
Jeremy's Hypertrophy System
Configuration File

Version: 1.1.0
"""

from pathlib import Path


# Application Information
APP_NAME = "Jeremy's Hypertrophy System"
APP_VERSION = "1.1.0"


# Base Directory
BASE_DIR = Path(__file__).resolve().parent


# Data Directory
DATA_DIR = BASE_DIR / "data"


# Database Location
DATABASE_PATH = DATA_DIR / "jhs.db"


# Interface Settings
THEME_MODE = "dark"

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800


# Training Defaults

DEFAULT_RIR = 2

DEFAULT_REST_TIME = 90


# Hypertrophy Rep Guidelines

DEFAULT_REP_MIN = 8
DEFAULT_REP_MAX = 12
