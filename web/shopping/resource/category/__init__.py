from flask import Blueprint
from flask_restful import Api
from shopping.resource.category.category_view import Category_View, Category_Index,Shopping_HomeNewProduct,\
    Shopping_RecommendProduct, ProjectProduct
category_bp = Blueprint('category', __name__)

category_api = Api(category_bp)

category_api.add_resource(Category_View, '/test')
category_api.add_resource(Category_Index, '/index')
category_api.add_resource(Shopping_HomeNewProduct, 'new')
category_api.add_resource(Shopping_RecommendProduct, '/hot')
category_api.add_resource(ProjectProduct, '/project')





