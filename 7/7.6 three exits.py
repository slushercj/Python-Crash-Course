# conditional
topping = ''
while topping != 'quit':
    topping = input("(Program #1) Enter a pizza topping: ")

    if topping != 'quit':
        print(f"I'll add {topping} to your pizza")

# active variable
active = True
while active:
    topping = input("(Program #2) Enter a pizza topping: ")

    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza")

# break statement
while True:
    topping = input("(Program #3) Enter a pizza topping: ")

    if topping == 'quit':
        break
    
    print(f"I'll add {topping} to your pizza")