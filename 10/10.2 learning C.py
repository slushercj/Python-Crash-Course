from pathlib import Path

path = Path('10/learning_python.txt')

contents = path.read_text().replace('Python', 'Rust')

print(f"{contents}")

print("\n\nNow printing line-by-line:")
lines = path.read_text().replace('Python', 'Rust').splitlines()

for line in lines:
    print(line)
