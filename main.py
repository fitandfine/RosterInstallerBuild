import os
import subprocess
import time
import sqlite3
import sys

from utils import get_appdata_dir  # ✅ Correct utility import

# ✅ Use %APPDATA%\BP_Eltham_Roster as working directory
APPDATA_FOLDER = get_appdata_dir()
DB_PATH = os.path.join(APPDATA_FOLDER, "roster.db")

# ✅ Proper path for init_setup.exe (always next to main.exe)
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INIT_SETUP_PATH = os.path.join(BASE_DIR, "init_setup", "init_setup.exe")

# Check DB validity
def db_valid(path):
    try:
        with sqlite3.connect(path) as con:
            con.execute("SELECT COUNT(*) FROM managers")
        return True
    except:
        return False

# Run setup if DB missing/corrupt
if not os.path.exists(DB_PATH) or not db_valid(DB_PATH):
    try:
        subprocess.run([INIT_SETUP_PATH], check=True)

    except Exception as e:
        raise RuntimeError(f"Failed to initialize database.\nError: {e}")

    for _ in range(50):
        if db_valid(DB_PATH):
            break
        time.sleep(0.1)

    if not db_valid(DB_PATH):
        raise RuntimeError("Database initialization failed. Exiting.")

# Launch login screen
import login
