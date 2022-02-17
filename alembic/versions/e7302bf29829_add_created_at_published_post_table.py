"""add_created_at_published_post_table

Revision ID: e7302bf29829
Revises: c8e80330fe40
Create Date: 2022-02-16 23:03:14.276300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7302bf29829'
down_revision = 'c8e80330fe40'
branch_labels = None
depends_on = None


def upgrade():

    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))

    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                            server_default=sa.text('NOW()'), nullable=False))
    pass


def downgrade():
    op.drop_column(table_name='posts', column_name='created_at')
    op.drop_column(table_name='posts', column_name='published')
    pass
