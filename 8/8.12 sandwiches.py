def make_sandwich(*ingredients):
    """Returns the tuple of ingredients passed in"""
    return ingredients

meatball_sandwich = make_sandwich('italian bread', 'meatballs')
air_sandwich = make_sandwich()
ham_and_cheese_sandwich = make_sandwich('ham', 'mozarella', 'white')

print(meatball_sandwich)
print(air_sandwich)
print(ham_and_cheese_sandwich)