favorite_places = {
    'chris': ['usa', 'uk', 'New Zealand'],
    'yorgelis': ['Egypt', 'usa', 'Venezuela'],
    'marlyn': ['usa', 'belize', 'carribean'],
    'walter': ['belize']
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")

    for place in places:
        if place == 'uk' or place == 'usa':
            print(place.upper())
        else:
            print(place.title())