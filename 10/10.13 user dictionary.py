from pathlib import Path
import json


def get_stored_user_information(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_information = json.loads(contents)
        return user_information
    else:
        return None

def get_user_information(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    age = input("How old are you?")
    favorite_quote = input("What's your favorite quote?")

    user_information = {'username': username, 'age': age, 'favorite_quote': favorite_quote}

    contents = json.dumps(user_information)
    path.write_text(contents)

    return user_information

def greet_user():
    """Greet the user by name."""
    path = Path('10/user_information.json')
    user_information = get_stored_user_information(path)

    if user_information:
        print(f"Welcome back, {user_information["username"]}! You are {user_information["age"]} and your favorite quote is '{user_information["favorite_quote"]}'")
    else:
        user_information = get_user_information(path)
        print(f"We'll remember you when you come back, {user_information["username"]}!")

greet_user()