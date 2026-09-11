sandwich_orders = ['meatball', 'pastrami', 'pastrami', 'italian', 'reuben', 'pastrami', 'cuban']
finished_sandwiches = []

print('The Deli has run out of pastrami!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("Sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")