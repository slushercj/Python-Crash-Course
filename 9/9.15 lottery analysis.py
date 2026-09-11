from random import sample

# Renamed 'list' to 'pool' and fixed '4' to integer 4
pool = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')
my_ticket = [8, 'b', 4, 2] 

def get_new_numbers():
    return sample(pool, 4)

def is_matching_ticket(my_ticket, winning_numbers):
    for number in my_ticket:
        if number not in winning_numbers:
            return False
    return True

is_match = False
run_count = 0

while not is_match:
    run_count += 1
    winning_ticket = get_new_numbers()
    is_match = is_matching_ticket(my_ticket, winning_ticket)

print(f"It took {run_count} tries for my ticket to match!")