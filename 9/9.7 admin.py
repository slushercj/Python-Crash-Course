class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 43
        self.user_id = 1
        self.membership_level = 'Silver'

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and a {self.membership_level} user.")

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}.")

class Admin(User):

    def __init__(self, first_name, last_name, *privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

admin = Admin('Yorgelis', 'Andrade', 'Can ban user', 'Can delete post')

admin.show_privileges()