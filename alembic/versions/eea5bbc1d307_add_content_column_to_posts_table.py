"""add content column to posts table

Revision ID: eea5bbc1d307
Revises: 4b93780f213e
Create Date: 2021-12-31 11:51:33.758741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eea5bbc1d307'
down_revision = '4b93780f213e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
