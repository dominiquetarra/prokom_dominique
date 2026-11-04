def make_sandwich(*toppings):
    """Make a sandwich with the given items."""
    print("\nMaking sandwich with the following toppings : ")
    for topping in toppings :
        print(f"- {topping}")

make_sandwich('smoked beef', 'cheddar cheese')
make_sandwich('tuna')
make_sandwich('peanut butter', 'strawberry jam')