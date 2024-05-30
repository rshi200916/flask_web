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


def email(email):

    if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
        return email
    else:
        raise ValueError('this is a wrong email')


