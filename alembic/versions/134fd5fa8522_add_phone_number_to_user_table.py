"""add phone_number to user table 

Revision ID: 134fd5fa8522
Revises: 898e196d97b3
Create Date: 2021-12-31 15:33:42.653181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '134fd5fa8522'
down_revision = '898e196d97b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
