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
        self.privileges = Privileges (["can add post" , "can delete post" , "can ban user"])

class Privileges :
    def __init__(self, privileges=[]) :
        self.privileges = privileges

    def show_privileges(self) :
        print(f"Privilages = {self.privileges}")
    

admin = Admin ("Thomas" , "Robert" , "th_robert" , "25")
admin.describe_user()
admin.privileges.show_privileges()