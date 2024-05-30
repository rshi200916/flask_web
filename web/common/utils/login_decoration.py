from flask import g


def login_required(func):

    def wrapper(*args, **kwargs):
        if g.user_id is not None:
            return func(*args, **kwargs)

        return {
            'message': 'invalid token, required login',
            'code': "401",
        }
    return wrapper
