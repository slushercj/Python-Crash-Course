class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 43
        self.user_id = 1
        self.membership_level = 'Silver'
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and a {self.membership_level} user.")

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

chris = User('Christopher', 'Slusher')

for i in range(3):
    chris.increment_login_attempts()

print(chris.login_attempts)

chris.reset_login_attempts()

print(chris.login_attempts)