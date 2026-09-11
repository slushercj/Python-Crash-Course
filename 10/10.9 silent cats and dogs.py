from pathlib import Path

cats_path = Path('10/cats.txt')
dogs_path = Path('10/dogs.txt')

try:
    cats_content = cats_path.read_text()
except FileNotFoundError:
    pass
else:
    print(cats_content)

try:
    dogs_content = dogs_path.read_text()
except FileNotFoundError:
    pass
else:
    print(dogs_content)
