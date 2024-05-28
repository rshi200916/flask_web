class Config(object):
    HostName = '127.0.0.1'
    Port = '3306'
    DATABASE = 'back'
    USERNAME = 'back'
    PASSWORD = '123456'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HostName, Port,DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATION = False

    LOGGING_LEVEL = 'DEBUG' #日志级别
    LOGGING_FILE_DIR = '/log' #日志放置的目录
    LOGGING_FILE_MAX_BYTES = 300*1024*1024 #日志文件的大小
    LOGGING_FILE_BACKUP = 10  #日志文件保存的数量
    #redis 存储验证信息
    RATELIMIT_STORAGE_URL = 'redis://127.0.0.1:6379/0'
    RATELIMIT_STRATEGY = 'moving-window'
    REDIS_URL = 'redis://127.0.0.1:6379/1'








class DevelopConfig(Config):

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductConfig(Config):
    pass

