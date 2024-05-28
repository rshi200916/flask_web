from flask import Flask
from settings import map_config
from common.models import db
from shopping.resource.user import user_bp
from common.utils.logger.flask_logger import create_logger


def create_app(config_type):
    app = Flask(__name__)
    app.config.from_object(map_config.get(config_type))
    #db的初始化
    db.init_app(app)
    #用户蓝图的加载
    app.register_blueprint(user_bp, url_prefix='/user')
    #日志
    create_logger(app)
    #限流器
    from common.utils.limiter import limiter as lm
    lm.init_app(app)
    #redis初始化
    from common.utils.redis_cli import RedisClient
    RedisClient.init_app(app)
    return app