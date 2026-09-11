sandwich_orders = ['meatball', 'italian', 'reuben', 'cuban']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("Sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")