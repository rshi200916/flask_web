import json
from random import random

from flask_restful import Resource
from common.models import db
from flask_restful import reqparse
from common.models.category import Category
from common.utils.data2dict import datas2dict
from common.utils.redis_cli import RedisClient
from common.utils import constance
from common.models.category import Product, HomeNewProduct, HomeRecommendProduct, HomeProjectProduct,ProjectCategory


#数据测试资源类
class Category_View(Resource):
    def get(self):
        print("start")
        cate = Category.query.with_entities(Category.id, Category.ch,  Category.en).filter(Category.status == 1).all()
        # cate = Category.query.filter(Category.status == 1).all()
        # print(len(cate))
        print(type(cate))
        print(type(cate[0]))
        #在有with_entities时返回的时list(多个数据)list中里面时sqlalchemy.engine.row.Row对象其中的_data里面存的的是数据，_fields里面存的是key值
        #没有with_entities时返回的时db.Model对象，其__dict__中存储着数据和key值
        # for da in cate:
            # print(type(da))
            # print(da._data)
            # print(da._fields)
            # dict_data = [dict(zip(da._fields, da._data))]
            # type(dict_data)
            # print(da.__dict__)
            # print(isinstance(da, db.Model))
        # data_list = [dict(zip(da._fields, da._data)) for da in cate]
        # print(type(cate[0]))
        # print(isinstance(cate[0], db.Model))
        # for ca in cate:
        #     ca.__dict__.pop('_sa_instance_state')
        # data_list = [item.__dict__ for item in cate]
        # print(data_list)
        return {
            "message": "查询完成",
            "code": "200",
        }

#这个是首页面的数据请求的资源类
class Category_Index(Resource):
    def get(self):
        data_cache = RedisClient.get("category_index")
        if data_cache:#如果redis中有缓存的数据，(将字符串转成字典)
            return json.loads(data_cache)
        else:
            rq = reqparse.RequestParser()
            args = rq.add_argument('parent_id', required=True, type=int)
            parent_id = args.parent_id
            data = self.getDate(parent_id)
            if data:
                for item in data:
                    item.update({"list": ''})
                    second_data = self.getDate(item["id"])
                    item["list"] = second_data
                    for l_item in second_data:
                        l_item.update({"list": ''})
                        third_data = self.getDate(l_item["id"])
                        l_item["list"] = third_data
                RedisClient.setex('category_index', constance.CATEGORY_EXPIRED_TIME, json.dumps(data))
                return data
            else:
                return {
                    "message": "数据空了",
                    'code': '401'
                }
        #这个是不使用缓存的
        # rq = reqparse.RequestParser()
        # args = rq.add_argument('parent_id', required=True, type=int)
        # parent_id = args.parent_id
        # data = self.getDate(parent_id)
        # if data:
        #     for item in data:
        #         item.update({"list": ''})
        #         second_data = self.getDate(item["id"])
        #         item["list"] = second_data
        #         for l_item in second_data:
        #             l_item.update({"list": ''})
        #             third_data = self.getDate(l_item["id"])
        #             l_item["list"] = third_data
        #     return data
        # else:
        #     return {
        #         "message": "数据空了",
        #         'code': '401'
        #     }

    @staticmethod
    def getDate(parent_id):
        cate = Category.query.filter(Category.status == parent_id).all()
        if cate:
            dict_data = datas2dict(cate)
            return dict_data
        else:
            return None

#首页新品推荐资源类
class Shopping_HomeNewProduct(Resource):
    def get(self):
        res = HomeNewProduct.query.join(Product, HomeNewProduct.product_id == Product.id).with_entities(
            Product.product_name, Product.price, Product.id, Product.default_pic, Product.rel_category3_id).order_by(
            Product.product_no).limit(10).all()

        if res:
            return datas2dict(res)

        else:
            return {
                'message': '数据空了',
                'code': '401'
            }


#火热商品推荐资源类(使用redis缓存)
class Shopping_RecommendProduct(Resource):
    def get(self):
        data_cache = RedisClient.get("shopping_recommend")
        if data_cache:  # 如果redis中有缓存的数据，(将字符串转成字典)
            return json.loads(data_cache)
        else:
            data = HomeRecommendProduct.query.join(Product, HomeRecommendProduct.product_id == Product.id).with_entities
            (Product.product_name, Product.price, Product.id, Product.default_pic,Product.rel_category3_id).order_by(
                Product.product_no).limit(10).all()
            if data:
                RedisClient.setex('shopping_recommend', constance.CATEGORY_EXPIRED_TIME, json.dumps(data))
                return datas2dict(data)
            else:
                return {
                    'message': '数据空了',
                    'code': '401'
                }


#商品主题资源类
class ProjectProduct(Resource):
    def get(self):
        data_cache = RedisClient.get('shopping_project')
        if data_cache:
            return json.loads(data_cache)
        else:
            project = HomeProjectProduct.query.filter(HomeProjectProduct.show_status == 1).all()
            if project:
                data = datas2dict(project)
                for i in range(len(data)):
                    res_pro = ProjectCategory.query.join(Product, ProjectCategory.product_id == Product.id).filter\
                       (ProjectCategory.project_id == data[i]['id']).\
                       with_entities(Product.product_no, Product.product_name, Product.price, Product.default_pic,
                                     Product.rel_category3_id).limit(10).all()
                    if res_pro:
                        data[i]['product_list'] = datas2dict(res_pro)
                    else:
                        data[i]['product_list'] = ''
                    RedisClient.setex('shopping_project', constance.CATEGORY_EXPIRED_TIME, json.loads(data))
                    return data
            else:
                return {
                   'message': '数据空了',
                   'code': '401'
                }
















