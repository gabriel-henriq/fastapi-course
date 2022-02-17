"""Create content_column_to_post_table

Revision ID: 95406f39a575
Revises: 492c7326824c
Create Date: 2022-02-16 22:27:27.643530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95406f39a575'
down_revision = '492c7326824c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
