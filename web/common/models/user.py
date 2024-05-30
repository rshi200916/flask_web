from common.models import db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):

    __tablename__ = 't_user'

    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True, doc='用户ID')
    username = db.Column(db.String(64), doc='用户名', nullable=False, unique=True)
    password = db.Column(db.String(256), doc='密码', nullable=False)
    icon = db.Column(db.String(5000), doc='用户图像')
    email = db.Column(db.String(100), doc='电子邮件')
    phone = db.Column(db.String(11), doc='电话号码')
    create_time = db.Column(db.DateTime, default=datetime.now(), doc='创建时间')
    login_time = db.Column(db.DateTime, default=datetime.now(), doc='登录时间')
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), doc='更新时间')
    status = db.Column(db.Integer, default=1, doc='用户状态')

    @property
    def pwd(self):
        return self.password

    @pwd.setter
    def pwd(self, c_password):

        self.password = generate_password_hash(c_password)

    @property
    def check_password(self, c_password):

        return check_password_hash(self.password, c_password)
    






