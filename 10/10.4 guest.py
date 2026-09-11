from pathlib import Path

name = input('What is your name?')
path = Path('10/guest.txt')

path.write_text(name)