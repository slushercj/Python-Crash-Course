class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restuarant's name is {self.restaurant_name} and serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")

trulucks = Restaurant("Truluck's", 'seafood')
taste_of_the_himilayas = Restaurant('Taste of the Himilayas', 'indian')
gyu_kaku = Restaurant('Gyu-Kaku', 'japanese')

trulucks.describe_restaurant()
trulucks.open_restaurant()

taste_of_the_himilayas.describe_restaurant()
taste_of_the_himilayas.open_restaurant()

gyu_kaku.describe_restaurant()
gyu_kaku.open_restaurant()