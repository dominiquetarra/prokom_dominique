responses = {}
polling_active = True
while polling_active :
    #Prompt for the person's name and place
    name = input("\nWhat's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    #store the responses in dictionary
    responses[name] = place

    #Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat.lower() == 'no' :
        polling_active = False

#Polling is complete. Showing the results
print("\n---Poll Results---")
for name, place in responses.items() :
    print(f"{name.title()} would love to go to {place.title()}")