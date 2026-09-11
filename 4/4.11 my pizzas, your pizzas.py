pizzas = ["Hawaiian", "Bacon & Pepperoni", "Supreme", "BBQ Chicken"]
friend_pizzas = pizzas[:]

pizzas.append("Margherita")
friend_pizzas.append("Mexican")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)