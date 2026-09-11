current_users = ['admin', 'cslusher', 'codeboss', 'slusher.cj', 'user456']

new_users = ['codeboss', 'cslusher', 'alavic', 'toxicLeah']

lowercase_current_users = []

for user in current_users:
    lowercase_current_users.append(user.lower())

for new_user in new_users:
    if new_user.lower() in lowercase_current_users:
        print(f"Username {new_user} taken, please choose a new username")
    else:
        print(f"{new_user} available")