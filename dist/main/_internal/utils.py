# utils.py
import os

def get_appdata_dir():
    """
    Returns a consistent app-specific folder in %APPDATA%.
    Creates it if it doesn't exist.
    """
    path = os.path.join(os.environ.get("APPDATA"), "BP_Eltham_Roster")
    os.makedirs(path, exist_ok=True)
    return path
