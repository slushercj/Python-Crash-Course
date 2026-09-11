poll_active = True
results = {}

while poll_active:
    name = input("What's your name? ")
    dream_vacation = input("If you could visit one place in the world, where would you go?: ")

    results[name] = dream_vacation

    should_continue = input("Do you want to take another poll? (yes/no): ")

    if should_continue == 'no':
        poll_active = False

print("Results of poll:")
for name, destination in results.items():
    print(f"{name}'s dream destination is {destination}.")