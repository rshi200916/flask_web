import random
from typing import Iterable

from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from common.models.user import User
from common.utils.limiter import limiter as lmt
from flask_limiter.util import get_remote_address
from common.utils import constance
from flask import request, current_app
from common.utils.redis_cli import RedisClient
from common.utils import paraser



class UserView(Resource):
    def get(self):
        print('hello world')
        # current_app.logger
        if isinstance(current_app.logger, Iterable):
            for t in current_app.logger:
                print(t)
        # current_app.logger.info('我的日志')
        return {'hello': 'world'}


class TestLimiterView(Resource):
    decorators = [

        lmt.limit(constance.LIMITER_BY_PARA, key_func=lambda: request.args['key'], error_message="To Many Times, Clam Down Bro"),
        lmt.limit(constance.LIMITER_BY_IP, key_func=get_remote_address, error_message="To Many Times, Clam Down Bro")
    ]

    def get(self):
        para = request.args.get('key')
        code = random.randint(1000, 9999)
        try:
            RedisClient.setex('shopping:sms:{}'.format(para), constance.REDIS_SMS_EXPIRE, code)

        except:
            return {
                'message': '发送验证码失败',
                'code': 400,
            }

        return {
            'message': '验证码发送成功',
            'sms_code': code,
            'code': 200,
        }


class CodeAUTH(Resource):

    def post(self):
        rq = RequestParser()
        rq.add_argument('phone', type=paraser.mobile, required=True, location='form')
        rq.add_argument('code', type=paraser.regex(r'^\d{4}$'), required=True, location='form')
        args = rq.parse_args()
        phone = args.phone
        code = args.code
        key = 'shopping:sms:{}'.format(phone)
        try:
            real_code = RedisClient.get(key)
            print(real_code)

        except ConnectionError as e:
            # current_app.logger.error(e)
            return {
                'message': '服务器出现错误',
                'code': '404',
            }

        if not real_code and code != real_code:
            return {
                'message': '验证码错误',
                'code': '400',
            }
        return {
            'phone': phone,
            'message': '验证成功',
        }




