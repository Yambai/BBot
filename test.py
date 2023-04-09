import pickle
'''with open('users_id.hui', 'rb') as f:
    users = pickle.load(f)
    print(users,'-------0')'''
'''users = {1306241821}
with open('users_id.hui', 'wb') as f:
    pickle.dump(users, f)'''
with open('users_id.hui', 'rb') as f:
    users = pickle.load(f)
    print(users,'-------1')
