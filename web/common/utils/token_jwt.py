import jwt
from datetime import datetime, timedelta

from common.models.user import User
from common.utils import constance
from jwt import PyJWTError
from flask import current_app


def generate_token(user_id):
    payload = {
        'id': user_id,
        'exp': datetime.utcnow() + timedelta(days=constance.TOKEN_EXPIRED_DAY_TIME)
    }
    data = jwt.encode(payload=payload, key=constance.TOKEN_KEY, algorithm='HS256')
    return data


def unzip_token(token_str):
    try:
        token_dict = jwt.decode(token_str, key=constance.TOKEN_KEY, algorithms='HS256')

    except PyJWTError as er:
        current_app.logger.info(er)
        return {
            'message': 'token验证错误',
            'code': '401',
        }
    user = User.query.filter(User.id == token_dict['id']).first()
    if not user and user.status != 1:
        return{
            'message': '用户状态过期',
            'code': '401',
        }
    return {
        'id': user.id,
    }


