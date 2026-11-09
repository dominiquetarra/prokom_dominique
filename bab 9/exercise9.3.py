class User :
    def __init__(self, first_name, last_name, username, age) :
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age

    def describe_user (self) :
        print(f"Full name = {self.first_name}")
        print(f"Last name = {self.last_name}")
        print(f"Username = {self.username}")
        print(f"Age = {self.age}")

    def greet_user (self) :
        print(f"Welcome back, {self.username}")

user1 = User("Domi" , "Tarra" , "domitarra" , "18")
user2 = User("Lala" , "Xandra" , "lala_xandra" , "20")
user3 = User("Thomas" , "Robert" , "thom4srob3rt" , "25")

#calling methods
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
