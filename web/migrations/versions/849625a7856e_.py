"""empty message

Revision ID: 849625a7856e
Revises: d26e1508671d
Create Date: 2024-06-03 21:20:08.925365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '849625a7856e'
down_revision = 'd26e1508671d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_project_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True, comment='专题id'),
    sa.Column('product_id', sa.Integer(), nullable=True, comment='商品id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_project_category')
    # ### end Alembic commands ###
