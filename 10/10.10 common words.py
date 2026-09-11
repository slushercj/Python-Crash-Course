from pathlib import Path

path = Path("10/the great gatsby.txt")
content = path.read_text().lower()

searched_word = 'rich'
count = content.count(searched_word.lower())

print(f"'{searched_word}' appears {count} times in {path}")