cities = {
    "tokyo" : {
        "country" : "japan" ,
        "population" : "13.9 million" , 
        "fact" : "The most populous metropolitan area in the world" ,
        "currency" : "Yen" , 
    },
    "paris" : {
        "country" : "france" ,
        "population" : "2.1 million" , 
        "fact" : "Famous for the Eiffel Tower" , 
        "currency" : "Euro" , 
    },
    "jakarta" : {
        "country" : "indonesia" , 
        "population" : "10 million" , 
        "fact" : "Capital city of Indonesia" ,
        "currency" : "Egyptian Pound"
    },
}
for city, cityInfo in cities.items() :
    print(f"\nCity : {city.title()}")
    print(f"Country : {cityInfo['country'].title()}")
    print(f"Population : {cityInfo['population']}")
    print(f"Fact : {cityInfo['fact']}")
    print(f"Currency : {cityInfo['currency']}")