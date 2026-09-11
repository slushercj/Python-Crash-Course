def add():
    input1 = input("Enter the first number: ")

    try:
        input1 = int(input1)
    except ValueError:
        print(f"'{input1}' is not a number")
        return

    input2 = input("Enter the second number: ")

    try:
        input2 = int(input2)
    except ValueError:
        print(f"'{input2}' is not a number")
        return

    print(f"The result is {input1 + input2}")

add()