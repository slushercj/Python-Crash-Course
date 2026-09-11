favorite_numbers = {
    'chris': [82, 8, 2],
    'yennefer': [8],
    'morrigan': [7],
    'walter': [1],
    'raistlin': [666, 3.14]
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are:")

    for number in numbers:
        print(number)
    