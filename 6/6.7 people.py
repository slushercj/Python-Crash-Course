person1 = {
    'first_name': 'Leah',
    'last_name': 'Slusher',
    'age': 12,
    'city': 'Ensenada',
}

person2 = {
    'first_name': 'Chris',
    'last_name': 'Slusher',
    'age': 43,
    'city': 'San Diego',
}

person3 = {
    'first_name': 'Yorgelis',
    'last_name': 'Andrade',
    'age': 29,
    'city': 'Dallas',
}

people = [person1, person2, person3]

for person in people:
    print(f"{person['first_name']} {person['last_name']} is age {person['age']} and lives in {person['city']}.")