cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 37.7,
        'fact': 'is the world\'s most populous metropolitan area'
    },
    'Delhi': {
        'country': 'India',
        'population': 32.2,
        'fact': 'ranking as the second-largest megacity globally'
    },
    'Shanghai': {
        'country': 'China',
        'population': 24.9,
        'fact': 'is serving as a major global financial hub'
    },
}

for city, city_info in cities.items():
    print(f"\n{city.title()}:")

    print(f"{city.title()} is a city in {city_info['country']}.  It has a population of {city_info['population']}M and {city_info['fact']}.")