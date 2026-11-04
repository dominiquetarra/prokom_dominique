pet1 = {"kind" : "dog" , "owner" : "elle"}
pet2 = {"kind" : "cat" , "owner" : "sarah"}
pet3 = {"kind" : "bird" , "owner" : "tomi"}

pets = [pet1 , pet2 , pet3]

for pet in pets :
    print(f"\n{pet['owner']} has a {pet['kind']}")