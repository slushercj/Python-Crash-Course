from pathlib import Path

contents = ''
while True:
    name = input("What is your name? (Type 'quit' to exit)")

    if name == 'quit':
        break

    contents += f"{name}\n"
    
path = Path('10/guest_book.txt')
path.write_text(contents)