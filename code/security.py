from werkzeug.security import safe_str_cmp

from user import User


def authenticate(username, password):
    user = User.findbyusername(username)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.findbyid(user_id)


if __name__ == '__main__':
    res = authenticate('Samuels', 'abcxyz')
    iden = identity(res)
    print(iden)
    # print(res.__dict__)

# res = authenticate('Samuel', 'abcxyz')
