def city_country (city, country) :
    name = f"{city.title()}, {country.title()}"
    return name

city = city_country('jakarta', 'indonesia')
print(city)

city = city_country('tokyo', 'japan')
print(city)

city = city_country('seoul', 'korea')
print(city)