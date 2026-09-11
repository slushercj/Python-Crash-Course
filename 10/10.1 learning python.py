from pathlib import Path

path = Path('10/learning_python.txt')

contents = path.read_text()

print(f"{contents}")

print("\n\nNow printing line-by-line:")
lines = path.read_text().splitlines()

for line in lines:
    print(line)
