"""add foreign-key to post table

Revision ID: 65dba5967df1
Revises: 7a0fc03dc055
Create Date: 2021-12-31 14:52:30.764928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65dba5967df1'
down_revision = '7a0fc03dc055'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
