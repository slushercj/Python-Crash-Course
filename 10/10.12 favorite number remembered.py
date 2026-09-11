from pathlib import Path
import json

path = Path('10/favorite_number.txt')

if not path.exists():
    favorite_number = int(input("What's your favorite number?"))
    content = json.dumps(favorite_number)
    path.write_text(content)
else:
    favorite_number = json.loads(path.read_text())
    print(f"I know your favorite number.  It's {favorite_number}!")