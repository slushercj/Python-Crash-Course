glossary = {
    'conditional': 'A statement whose result determines which code branch gets executed',
    'loop': 'Iterating over a collection',
    'dictionary': 'A collection of key-value pairs',
    'list': 'A collection of items in a specific order',
    'tuple': 'Denoted by parenthesis and defines an immutable list',
    'set': 'A collection of non-repeating values without any order',
    'slice': 'A part of a list',
    'range()': 'A way to quickly generate a sequence of integers',
    'len()': 'Gets the length of a list',
    'Error': 'There are many types of errors when a program does something unexpected'
}

for key, value in glossary.items():
    print(f"{key.title()}:\n\t{value}")