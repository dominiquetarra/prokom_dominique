cities = {
    "tokyo" : {
        "country" : "japan" ,
        "population" : "13.9 million" , 
        "fact" : "The most populous metropolitan area in the world" ,
    },
    "paris" : {
        "country" : "france" ,
        "population" : "2.1 million" , 
        "fact" : "Famous for the Eiffel Tower" , 
    },
    "jakarta" : {
        "country" : "indonesia" , 
        "population" : "10 million" , 
        "fact" : "Capital city of Indonesia"
    },
}
for city, cityInfo in cities.items() :
    print(f"\nCity : {city.title()}")
    country = cityInfo["country"]
    population = cityInfo["population"]
    fact = cityInfo["fact"]
    print(f"Country : {country.title()}")
    print(f"Population : {population}")