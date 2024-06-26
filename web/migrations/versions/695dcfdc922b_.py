"""empty message

Revision ID: 695dcfdc922b
Revises: 
Create Date: 2024-06-03 17:55:40.700299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '695dcfdc922b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_home_new_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True, comment='商品id，用于查询收用'),
    sa.Column('product_name', sa.String(length=255), nullable=True, comment='商品名称'),
    sa.Column('recommend_status', sa.Integer(), nullable=True, comment='推荐状态，0表示未推荐，1表示已推荐'),
    sa.Column('enable', sa.SmallInteger(), nullable=False, comment='逻辑删除0-未删除，1-已删除'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('change_person', sa.String(length=64), nullable=False, comment='更新人的名称'),
    sa.Column('create_person', sa.String(length=64), nullable=False, comment='创建人的名称'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('t_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_no', sa.String(length=64), nullable=True, comment='商品编号'),
    sa.Column('product_name', sa.String(length=255), nullable=True, comment='商品名字'),
    sa.Column('rel_tenant_id', sa.BigInteger(), nullable=True, comment='商户id'),
    sa.Column('rel_default_sku_id', sa.BigInteger(), nullable=True, comment='默认SKU'),
    sa.Column('rel_category1_id', sa.BigInteger(), nullable=True, comment='一级类目'),
    sa.Column('rel_category2_id', sa.BigInteger(), nullable=True, comment='二级类目'),
    sa.Column('rel_category3_id', sa.BigInteger(), nullable=True, comment='三级类目'),
    sa.Column('price', sa.Numeric(precision=11, scale=2), nullable=True, comment='商品价格'),
    sa.Column('default_pic', sa.String(length=512), nullable=True, comment='商品图片'),
    sa.Column('album_pics', sa.Text(), nullable=True, comment='商品组图'),
    sa.Column('sales_num', sa.Integer(), nullable=True, comment='销量'),
    sa.Column('detail_desc', sa.String(length=512), nullable=True, comment='商品详细描述'),
    sa.Column('publish_status', sa.SmallInteger(), nullable=True, comment='上架状态0->下架，1->上架'),
    sa.Column('enable', sa.SmallInteger(), nullable=False, comment='逻辑删除0-未删除，1-已删除'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('change_person', sa.String(length=64), nullable=False, comment='更新人的名称'),
    sa.Column('create_person', sa.String(length=64), nullable=False, comment='创建人的名称'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_product')
    op.drop_table('t_home_new_product')
    # ### end Alembic commands ###
