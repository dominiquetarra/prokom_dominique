class Restaurant:

    def __init__(self, restaurant_name, cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) :
        print(f"Restaurant Name : {self.restaurant_name}")
        print(f"Cuisine Type : {self.cuisine_type}")

    def open_restaurant (self) :
        print(f"{self.restaurant_name} is now open!")

#Ice cream stand sublass
class IceCreamStand(Restaurant) :
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla" , "Strawberry" , "Chocolate"]
    def show_flavors(self) :
        print(f"Available flavors : {self.flavors}")

my_stand = IceCreamStand("Scooped Cream")
my_stand.describe_restaurant()
my_stand.show_flavors()