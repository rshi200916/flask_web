import datetime
import decimal

import sqlalchemy.engine.row

from common.models import db


def datas2dict(res_obj):
    print(type(res_obj))
    if not res_obj:
        return {"message": "none"}
    elif len(res_obj) == 1:
        return data2dict(res_obj)
    else:
        if isinstance(res_obj[0], sqlalchemy.engine.row.Row):
            data_dict = [dict(zip(ca._fields, ca._data)) for ca in res_obj]
            return datalist_formate(data_dict)
        if isinstance(res_obj[0], db.Model):
            for ca in res_obj:
                ca.__dict__.pop('_sa_instance_state')
            dicts = [item.__dict__ for item in res_obj]
            print(dicts)
            # return datalist_formate(dicts)
            return dicts


def data2dict(res_obj):
    if isinstance(res_obj, sqlalchemy.engine.row.Row):
        data_dict = [dict(zip(ca._fields, ca._data)) for ca in res_obj]
        return datalist_formate(data_dict)
    if isinstance(res_obj, db.Model):
        for ca in res_obj:
            ca.__dict__.pop('_sa_instance_state')
        return datalist_formate([item.__dict__ for item in res_obj])


#时间类型转字符串，decimal转float型
def datalist_formate(dictlist):
    if not dictlist:
        return dictlist
    elif len(dictlist) > 1:
        for item in dictlist:
            for key in item.keys():
                if isinstance(item[key], datetime.datetime) or isinstance(item[key], datetime.date):
                    item[key] = str(item[key])
                if isinstance(item[key], decimal.Decimal):
                    item[key] = float(item[key])
    else:
        for key in dictlist.keys():
            if isinstance(dictlist[key], datetime.date) or isinstance(dictlist[key], datetime.datetime):
                dictlist[key] = str(dictlist[key])
            if isinstance(dictlist[key], decimal.Decimal):
                dictlist[key] = float(dictlist[key])
    return dictlist
