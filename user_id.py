import pickle
import asyncio


def open_users():
    with open('users_id.hui', 'rb') as f:
        users: object = pickle.load(f)
        return users
async def check_id(id: object) -> object:
    with open('users_id.hui', 'rb') as f:
        users = pickle.load(f)
    if id not in users:
        users.add(id)
        with open('users_id.hui', 'wb') as f:
            pickle.dump(users, f)
            print('users saved')
    else:
        print('Пользователь уже записан')

