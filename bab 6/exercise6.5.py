rivers = {"nile" : 'egypt' , "amazon" : "brazil" , "rhine" : "germany"}
for river , country in rivers.items() :
    print(f"The {river.title()} runs through {country.title()}")

print("\nName of each River :")
for river in rivers.keys() :
    print({river.title()})

print("\nName of each country :")
for country in rivers.values() :
    print({country.title()})