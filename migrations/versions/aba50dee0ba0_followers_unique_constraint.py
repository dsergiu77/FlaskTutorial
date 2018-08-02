"""followers unique constraint

Revision ID: aba50dee0ba0
Revises: be9b105eacdd
Create Date: 2018-08-02 11:01:27.920290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aba50dee0ba0'
down_revision = 'be9b105eacdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uix_follower_followed', 'followers', ['follower_id', 'followed_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uix_follower_followed', 'followers', type_='unique')
    # ### end Alembic commands ###
