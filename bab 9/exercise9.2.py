class Restaurant:

    def __init__(self, restaurant_name, cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) :
        print(f"Restaurant Name : {self.restaurant_name}")
        print(f"Cuisine Type : {self.cuisine_type}")

    def open_restaurant (self) :
        print(f"{self.restaurant_name} is now open!")

restaurant1 = Restaurant("Thai Cuisine" , "Thailand food")
restaurant2 = Restaurant("Bella Italia" , "Italian food")
restaurant3 = Restaurant("Taco Loco" , "Mexican food")

#calling all
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()