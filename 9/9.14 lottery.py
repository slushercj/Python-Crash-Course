from random import randint, choice

list = (1, 2, 3, 4, 5, 6 ,7 , 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

winning_combination = []
for _ in range(4):
    winning_combination.append(choice(list))

print(f"The winning ticket is {winning_combination}!")
