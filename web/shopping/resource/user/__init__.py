import flask_redis
from flask_restful import Api
from flask import Blueprint
from common.utils.output import output_json
from shopping.resource.user.user_view import UserView, TestLimiterView,CodeAUTH,UserRegister,UserLogin
from common.utils.token_auth import token_before_request

user_bp = Blueprint('user', __name__)

# #这个是整个蓝图的token请求钩子
# user_bp.before_request(token_before_request)

user_api = Api(user_bp)
user_api.add_resource(UserView, '/test')
user_api.add_resource(TestLimiterView, '/sms')
user_api.add_resource(CodeAUTH, '/auth')
user_api.add_resource(UserRegister, '/register')
user_api.add_resource(UserLogin, '/login')
#在此处添加user蓝图的返回响应添加
# user_api.representation('application/json')(output_json)

