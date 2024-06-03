from datetime import datetime

from common.models import db

#商品类别表
class Category(db.Model):
    __tablename__ = 't_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ch = db.Column(db.String(128), comment="商品中文名称")
    en = db.Column(db.String(128), comment="商品的英文名称")
    level = db.Column(db.Integer, default=1, comment="商品层级")
    parent_id = db.Column(db.BigInteger, default=0, comment="父ID")
    cart_id = db.Column(db.Integer, comment="类目ID，关联parent_id使用")
    status = db.Column(db.SmallInteger, default=1, comment="状态，1表示正常，0表示下")
    weight = db.Column(db.Float, comment="类目单元配重")
    create_time = db.Column(db.DateTime, default=datetime.now(), comment='种类创建创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), comment='更新时间')
    change_person = db.Column(db.String(64), nullable=False, comment="更新人的名称", default='0')
    create_person = db.Column(db.String(64), nullable=False, comment="创建人的名称", default="0")
    enable = db.Column(db.SmallInteger, default=0, comment="是否删除，0未删除，1已删除", nullable=False)
    merchant = db.Column(db.String(64), comment="商户ID")

#产品表
class Product(db.Model):
    __tablename__ = 't_product'
    id = db.Column(db.Integer, primary_key=True)
    product_no = db.Column(db.String(64), comment="商品编号")
    product_name = db.Column(db.String(255), comment="商品名字")
    rel_tenant_id = db.Column(db.BigInteger, comment="商户id")
    rel_default_sku_id = db.Column(db.BigInteger, comment="默认SKU")
    rel_category1_id = db.Column(db.BigInteger, comment='一级类目')
    rel_category2_id = db.Column(db.BigInteger, comment='二级类目')
    rel_category3_id = db.Column(db.BigInteger, comment='三级类目')
    price = db.Column(db.Numeric(11, 2), comment='商品价格')
    default_pic = db.Column(db.String(512), comment='商品图片')
    album_pics = db.Column(db.Text, comment='商品组图')
    sales_num = db.Column(db.Integer, comment="销量")
    detail_desc = db.Column(db.String(512), comment='商品详细描述')
    publish_status = db.Column(db.SmallInteger, comment='上架状态0->下架，1->上架')
    enable = db.Column(db.SmallInteger, nullable=False, comment='逻辑删除0-未删除，1-已删除')
    create_time = db.Column(db.DateTime, default=datetime.now(), comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), comment='更新时间')
    change_person = db.Column(db.String(64), nullable=False, comment="更新人的名称", default='0')
    create_person = db.Column(db.String(64), nullable=False, comment="创建人的名称", default="0")
    # merchant = db.Column(db.String(64), comment="商户ID")

#新品推荐表
class HomeNewProduct(db.Model):
    __tablename__ = 't_home_new_product'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, comment='商品id，用于查询收用')
    product_name = db.Column(db.String(255), comment='商品名称')
    recommend_status = db.Column(db.Integer, comment='推荐状态，0表示未推荐，1表示已推荐')
    enable = db.Column(db.SmallInteger, nullable=False, comment='逻辑删除0-未删除，1-已删除')
    create_time = db.Column(db.DateTime, default=datetime.now(), comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), comment='更新时间')
    change_person = db.Column(db.String(64), nullable=False, comment="更新人的名称", default='0')
    create_person = db.Column(db.String(64), nullable=False, comment="创建人的名称", default="0")
    # merchant = db.Column(db.String(64), comment="商户ID")


#人气商品推荐表
class HomeRecommendProduct(db.Model):
    __tablename__ = 't_recommend_product'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, comment='商品id')
    product_name = db.Column(db.String(255), comment='商品名称')
    recommend_status = db.Column(db.Integer, comment='推荐状态，0表示未推荐，1表示已推荐')
    create_time = db.Column(db.DateTime, default=datetime.now(), comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), comment='更新时间')
    change_person = db.Column(db.String(64), nullable=False, comment="更新人的名称", default='0')
    create_person = db.Column(db.String(64), nullable=False, comment="创建人的名称", default="0")
    enable = db.Column(db.SmallInteger, nullable=False, comment='逻辑删除0-未删除，1-已删除')
    merchant = db.Column(db.Integer, comment="商户ID")


#商品专题表
class HomeProjectProduct(db.Model):
    __tablename__ = 't_project'
    id = db.Column(db.Integer, primary_key=True)
    subject_category_id = db.Column(db.BigInteger, comment='专题分类id')
    title = db.Column(db.String(244), comment='专题标题')
    pic = db.Column(db.String(500), comment='专题主图')
    product_count = db.Column(db.Integer, comment='关联产品数量')
    recommend_status = db.Column(db.Integer, comment='推荐状态')
    create_time = db.Column(db.DateTime, default=datetime.now(), comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), comment='更新时间')
    change_person = db.Column(db.String(64), nullable=False, comment="更新人的名称", default='0')
    create_person = db.Column(db.String(64), nullable=False, comment="创建人的名称", default="0")
    enable = db.Column(db.SmallInteger, nullable=False, comment='逻辑删除0-未删除，1-已删除')
    merchant = db.Column(db.Integer, comment="商户ID")
    show_status = db.Column(db.Integer, comment='显示状态，0不显示，1显示')
    forward_count = db.Column(db.Integer, comment='转发数')
    hot_words = db.Column(db.String(500), comment='专题热词')


#专题分类表
class ProjectCategory(db.Model):
    __tablename__ = 't_project_category'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, comment='专题id')
    product_id = db.Column(db.Integer, comment='商品id')









    


