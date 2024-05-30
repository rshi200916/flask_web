import os
LIMITER_BY_PARA = '1/minute'
LIMITER_BY_IP = '10/hour'
REDIS_SMS_EXPIRE = 1 * 60


TOKEN_EXPIRED_DAY_TIME = 3

TOKEN_KEY = os.urandom(10)
