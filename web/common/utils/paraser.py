import re


def mobile(mobile_str):
    if re.match(r'^13[0-9][0-9]{8}$', mobile_str):
        return mobile_str
    else:
        raise ValueError('{} is not a china phone'.format(mobile_str))


def regex(pattern):

    def auth(code_str):
        if re.match(pattern,code_str):
            return code_str
        else:
            return ValueError('please input right code')


    return auth