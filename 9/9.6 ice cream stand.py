class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = []

    def describe_restaurant(self):
        print(f"The restuarant's name is {self.restaurant_name} and serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")

class IceCreamStand(Restaurant):

    def __init__(self, *flavors):
        super().__init__('Handels', 'ice cream')
        self.flavors = flavors

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

handels = IceCreamStand('cookies and cream', 'chocolate chip cookie dough', 'butter pecan')
handels.display_flavors()