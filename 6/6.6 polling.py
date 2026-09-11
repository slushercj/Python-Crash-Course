favorite_languages = {  
    'jen': 'python',  
    'sarah': 'c',  
    'edward': 'rust',  
    'phil': 'python',  
} 

should_take_poll = ['chris', 'leah', 'jen', 'marlyn', 'phil']

for candidate in should_take_poll:
    if candidate in favorite_languages:
        print(f"Thank you for taking the poll, {candidate.title()}!")
    else:
        print(f"{candidate.title()}, you should take the favorite language poll!")