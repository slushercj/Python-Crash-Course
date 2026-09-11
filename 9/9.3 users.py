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

chris = User('Christopher', 'Slusher')
leah = User('Leah', 'Slusher')

chris.describe_user()
chris.greet_user()

leah.describe_user()
leah.greet_user()