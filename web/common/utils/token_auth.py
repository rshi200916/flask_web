from flask import g, current_app
from flask import request
from common.utils.token_jwt import unzip_token


def token_before_request():
    g.user_id = None
    try:
        #jwt.decode()中的jwt参数需要的是字节数据bytes
        tokens = request.headers.get('token')

    except Exception as ex:
        current_app.logger.info('请求头中没有token')
        return
    data = unzip_token(tokens)
    g.user_id = data.get('id')












