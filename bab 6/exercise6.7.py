people1 = {"first_name" : "Dominique" , "last_name" : "Tarra" , "age" : 18 , "city" : "Solo"}
people2 = {"first_name" : "Jane" , "last_name" : "Hopper" , "age" : 15 , "city" : "Hawkins"}
people3 = {"first_name" : "Elle" , "last_name" : "Woods" , "age" : 21 , "city" : "Los Angeles"}

people = [people1 , people2 , people3]

for person in people :
    print(f"\nName : {person['first_name']} {person['last_name']}")
    print(f"Age : {person['age']}")
    print(f"City : {person['city']}")