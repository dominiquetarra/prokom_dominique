prompt = "\nPlease enter your age"
prompt += "\nEnter 'quit' when finished : "

while True :
    age = input(prompt)
    if age.lower() == 'quit' :
        break
    age = int(age)
    if age < 3 :
        print("Your ticket is free")
    elif age < 13 :
        print("Your ticket is $10")
    else :
        print("Your ticket is $15")