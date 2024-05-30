import random
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from flask import g
from common.models.user import User
from common.utils.limiter import limiter as lmt
from flask_limiter.util import get_remote_address
from common.utils import constance
from flask import request, current_app
from common.utils.redis_cli import RedisClient
from common.utils import paraser
from common.models import db
from common.models.user import check_password_hash
from common.utils.token_jwt import generate_token
from common.utils.login_decoration import login_required


class UserView(Resource):
    method_decorators = {
        'get': [login_required]
    }

    def get(self):
        print('hello world')
        # current_app.logger
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


class UserRegister(Resource):

    def post(self):
        rq = RequestParser()
        rq.add_argument('username', required=True, location='form')
        rq.add_argument('email', type=paraser.email, required=True, location='form')
        rq.add_argument('password', required=True, location='form')
        rq.add_argument('phone', required=True, location='form')
        args = rq.parse_args()
        username = args.username
        password = args.password
        phone = args.phone
        email = args.email
        u = User.query.filter(User.username == username).first()
        us = User.query.filter(User.phone == phone).first()
        if u:
            return {
                'message': "{} is already exists".format(username),
                'code': '400',
            }
        if us:
            return {
                'message': "{} is already exits".format(phone),
                'code': "401",
            }

        user = User(username=username, phone=phone, email=email, pwd=password)
        db.session.add(user)
        db.session.commit()
        # token = generate_token(user.id)
        return {
            'message': 'create count successfully',
            'code': '200',
            # 'token': token
        }


class UserLogin(Resource):
    def post(self):
        rq = RequestParser()
        rq.add_argument('username', required=True, location='form')
        rq.add_argument('password', required=True, location='form')
        args = rq.parse_args()
        username = args.username
        password = args.password
        user = User.query.filter(User.username == username).first()
        if check_password_hash(user.password, password):
            token = generate_token(user.id)
            return {
                'message': "login successfully",
                'code': '200',
                'token': token
                }
            # if g.user_id == user.id:
            #     return {
            #       'message': 'Login successfully',
            #       'code': '200',
            #       }
            # else:
            #     token = generate_token(user.id)
            #     return {
            #         'message': "login successfully",
            #         'code': '200',
            #         'token': token
            #     }
        else:
            return {
                'message': '用户名或密码错误',
                'code': '401',
            }














