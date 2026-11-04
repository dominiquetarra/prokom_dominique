#program 1 sebelum
def make_sandwich(*toppings):
    print("\nMaking sandwich with the following toppings : ")
    for topping in toppings :
        print(f"- {topping}")

make_sandwich('smoked beef', 'cheddar cheese')
make_sandwich('tuna')
make_sandwich('peanut butter', 'strawberry jam')

#program 1 sesudah
def make_sandwich(*toppings):
    """Make a sandwich with the given items."""
    print("\nMaking sandwich with the following toppings : ")
    for topping in toppings :
        print(f"- {topping}")

make_sandwich('smoked beef', 'cheddar cheese')
make_sandwich('tuna')
make_sandwich('peanut butter', 'strawberry jam')

#program 2 sebelum
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

#program 2 sesudah 
def make_car(manufacturer, model, **car_info):
    """Make a dictionary representing a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

#program 3 sebelum
def show_messages (messages) :
    for message in messages :
        print(message)

text_messages = ["Hi there!" , "How are you?"]
show_messages(text_messages)

#program 3 sesudah
def show_messages (messages) :
    """Print all messages in the list."""
    for message in messages :
        print(message)

text_messages = ["Hi there!" , "How are you?"]
show_messages(text_messages)