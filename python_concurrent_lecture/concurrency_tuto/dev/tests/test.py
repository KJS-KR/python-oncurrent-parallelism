import json
from pathlib import Path
from typing import Optional


BASE_DIR = Path(__file__).resolve().parent
json_path: str = str(BASE_DIR / "secrets.json")

print(json_path)
