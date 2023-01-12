"""empty message

Revision ID: cbe8a309fd66
Revises: ef619a433d5b
Create Date: 2023-01-12 21:34:12.474919

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cbe8a309fd66'
down_revision = 'ef619a433d5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
                    sa.Column('add_date', sa.DateTime(), nullable=False),
                    sa.Column('pub_date', sa.DateTime(), nullable=False),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=128), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('post',
                    sa.Column('add_date', sa.DateTime(), nullable=False),
                    sa.Column('pub_date', sa.DateTime(), nullable=False),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=128), nullable=False),
                    sa.Column('desc', sa.String(length=200), nullable=True),
                    sa.Column('content', mysql.LONGTEXT(), nullable=False),
                    sa.Column('category_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('tags',
                    sa.Column('tag_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
                    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
                    sa.PrimaryKeyConstraint('tag_id', 'post_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    op.drop_table('post')
    op.drop_table('tag')
    # ### end Alembic commands ###