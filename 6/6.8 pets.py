pet1 = {
    'type': 'tiger',
    'owner': 'Chris'
}
pet2 = {
    'type': 'cat',
    'owner': 'Monica'
}
pet3 = {
    'type': 'dog',
    'owner': 'Leah'
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet['owner']} has a {pet['type']}")