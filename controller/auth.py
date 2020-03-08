from werkzeug.security import safe_str_cmp
from model import Users


users = [
    Users.User(1, 'Kumindu Ranawaka','kumindu','kumindu2020'),
    Users.User(2, 'Elatech Solutions','elatech','elatech2020'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)