cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 37.7,
        'fact': 'has an urban population of 37.7 million, making it the world\'s most populous metropolitan area'
    },
    'Delhi': {
        'country': 'India',
        'population': 32.2,
        'fact': 'ranking as the second-largest megacity globally'
    },
    'Shanghai': {
        'country': 'China',
        'population': 24.9,
        'fact': 'serving as a major global financial hub'
    },
}

for city, city_info in cities.items():
    print(city.title())

    for k, v in city_info.items():
        print(f"{k}: {v}")