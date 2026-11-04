current_users = ['admin' , 'eric' , 'dominique' , 'fillaena' , 'yusrina']
new_users = ['dominique' , 'sarah' , 'Yusrina' , 'tomi' , 'FARA']
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users :
    if new_user.lower() in current_users_lower :
        print(f"{new_user}, is already used, please enter a new username.")
    else :
        print(f"{new_user} is available.")