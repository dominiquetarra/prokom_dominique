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

class Admin(User) :
    def __init__(self, first_name, last_name, username, age):
        super().__init__(first_name, last_name, username, age)
        self.privileges = ["can add post" , "can delete post" , "can ban user"]

    def show_privileges(self) :
        print(f"User privileges : {self.privileges}")

admin = Admin ("Sarah" , "Jones" , "sarah_j" , "28")
admin.describe_user()
admin.show_privileges()