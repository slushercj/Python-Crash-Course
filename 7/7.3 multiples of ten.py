number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of ten!")
else:
    print(f"{number} is not divisible by ten.")