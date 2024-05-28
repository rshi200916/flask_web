import logging
import os.path

from flask import request
import logging.handlers


class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)


def create_logger(app):
    logging_file_dir = app.config['LOGGING_FILE_DIR']
    logging_file_max_bytes = app.config['LOGGING_FILE_MAX_BYTES']
    logging_file_backup = app.config['LOGGING_FILE_BACKUP']
    logging_level = app.config['LOGGING_LEVEL']
    if os.path.isdir(logging_file_dir):
        pass
    else:
        os.mkdir(logging_file_dir)
    request_formate = RequestFormatter('[%(asctime)s] %(remote_addr)s %(url)s %(levelname)s %(module)s %(lineno)s: %(message)s')
    flask_file_handler = logging.handlers.RotatingFileHandler(filename=os.path.join(logging_file_dir, 'shopping.log'),
                                                              maxBytes=logging_file_max_bytes,
                                                              backupCount=logging_file_backup)
    flask_file_handler.setFormatter(request_formate)
    flask_logger = logging.getLogger('shopping')
    flask_logger.addHandler(flask_file_handler)
    flask_logger.setLevel(logging_level)
    #上面的是输出在文件上的

    #下面是输出在控制台的
    flask_console_logger = logging.StreamHandler()
    flask_console_logger.setFormatter(logging.Formatter('[%(asctime)s] %(url)s %(levelname)s %(module)s %(lineno)s: %(message)s'))
    if app.debug:
        flask_logger.addHandler(flask_console_logger)










