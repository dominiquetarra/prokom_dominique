from exercise9_12_module1 import User

class Admin(User) :
    def __init__(self, first_name, last_name, username, age):
        super().__init__(first_name, last_name, username, age)
        self.privileges = Privileges (["can add post" , "can delete post" , "can ban user"])

class Privileges :
    def __init__(self, privileges=[]) :
        self.privileges = privileges

    def show_privileges(self) :
        print(f"Privilages = {self.privileges}")