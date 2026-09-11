rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'danube': 'germany'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")