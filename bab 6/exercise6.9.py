favorite_places = {
    "sarah" : ["paris"] ,
    "fara" : ["bali" , "tokyo"] ,
    "tomi" : ["london" , "new york" , "rome"]
}
for name , place in favorite_places.items():
    print(f"\n{name.title()}'s favorite place are :")
    for place in place:
        print(f"{place.title()}")