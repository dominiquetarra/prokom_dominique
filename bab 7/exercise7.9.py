sandwich_orders = ['pastrami' , 'tuna' , 'pastrami' , 'avocado' , 'egg' , 'pastrami' , 'cheese']
finished_sandwiches = []
print(f"Sorry, we're out of pastrami today")
while 'pastrami' in sandwich_orders :
    sandwich_orders.remove('pastrami')
while sandwich_orders :
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)
print("\nThis sandwiches have been made : ")
for sandwich in finished_sandwiches :
    print (f"{sandwich.title()} sandwich")
    