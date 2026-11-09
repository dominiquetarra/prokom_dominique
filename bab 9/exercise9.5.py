class User :
    def __init__(self, first_name, last_name, username, age) :
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.login_attempts = 0

    def describe_user (self) :
        print(f"Full name = {self.first_name}")
        print(f"Last name = {self.last_name}")
        print(f"Username = {self.username}")
        print(f"Age = {self.age}")

    def greet_user (self) :
        print(f"Welcome back, {self.username}")

    def increment_login_attempts (self) :
        self.login_attempts += 1

    def reset_login_attempts (self) :
        self.login_attempts = 0

user1 = User("Domi" , "Tarra" , "domitarra" , "18")

#calling methods
user1.describe_user()
user1.greet_user()

#calling increment methods 
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

#print login attempts
print(f"Login attempts : {user1.login_attempts}")

#reset login atempts
user1.reset_login_attempts()
print(f"Login attempts (reset) : {user1.login_attempts}")
