#While statement
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

topping = ''

while topping.lower() != 'quit' :
    topping = input(prompt)
    if topping.lower() != 'quit' :
        print(f"I'll add {topping} on your pizza")

#Active variable
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

active = True
while active :
    topping = input(prompt)
    if topping.lower() == 'quit' :
        active = False
    else :
        print(f"I'll add {topping} on your pizza")

#Break statement
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True :
    topping = input(prompt)
    if topping.lower() == 'quit' :
        break
    else :
        print(f"I'll add {topping} on your pizza")