current_users = ['ted', 'red', 'bed', 'fed', 'led']
new_users = ['ted', 'red', 'steve', 'kap', 'mo']
for user in new_users:
    if user in current_users:
        print(user.capitalize() + " is in both lists! Please enter a new username")
    else:
        print(user.capitalize() + " only appears in one list")
