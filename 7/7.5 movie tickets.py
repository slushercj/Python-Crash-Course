active = True
while active:
    age = input("How old are you?: ")
    if age != 'quit':
        age = int(age)

        if age < 3:
            print("Your ticket is free!")
        elif age < 13:
            print("Your ticket is $10")
        else:
            print("Your ticket is $15")
    else:
        active = False