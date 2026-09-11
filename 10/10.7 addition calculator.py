def add():
    input1 = input("Enter the first number: ")

    if input1 == 'quit':
        return False
    
    try:
        input1 = int(input1)
    except ValueError:
        print(f"'{input1}' is not a number")
        return True

    input2 = input("Enter the second number: ")

    if input2 == 'quit':
        return False
    
    try:
        input2 = int(input2)
    except ValueError:
        print(f"'{input2}' is not a number")
        return True

    print(f"The result is {input1 + input2}")
    return True

while add():
    pass