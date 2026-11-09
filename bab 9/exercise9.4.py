class Restaurant:

    def __init__(self, restaurant_name, cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self) :
        print(f"Restaurant Name : {self.restaurant_name}")
        print(f"Cuisine Type : {self.cuisine_type}")

    def open_restaurant (self) :
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number) :
        self.number_served = number

    def increment_number_served (self, additional_customers) :
        self.number_served += additional_customers

restaurant = Restaurant("Wang Li Heng" , "Oriental")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

#print number of customers have been served
print(f"Number of customers served : {restaurant.number_served}")

#changing the value
restaurant.number_served = 10
print(f"Number of customers served (update) : {restaurant.number_served}")

restaurant.number_served = 30
print(f"Number of customers served (update) : {restaurant.number_served}")

restaurant.number_served = 50
print(f"Number of customers served (update) : {restaurant.number_served}")