import flask_redis
from flask_restful import Api
from flask import Blueprint
from common.utils.output import output_json
from shopping.resource.user.user_view import UserView, TestLimiterView,CodeAUTH

user_bp = Blueprint('user', __name__)

user_api = Api(user_bp)
user_api.add_resource(UserView, '/test')
user_api.add_resource(TestLimiterView, '/sms')
user_api.add_resource(CodeAUTH, '/auth')
#在此处添加user蓝图的返回响应添加
# user_api.representation('application/json')(output_json)

