from pathlib import Path
import json

path = Path('10/favorite_number.txt')

if path.exists():
    favorite_number = json.loads(path.read_text())
    print(f"I know your favorite number.  It's {favorite_number}!")