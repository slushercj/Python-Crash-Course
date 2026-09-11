def city_country(city, country, population = ''):
    if population:
        return f"{city}, {country} - {population}".title()
    else:
        return f"{city}, {country}".title()