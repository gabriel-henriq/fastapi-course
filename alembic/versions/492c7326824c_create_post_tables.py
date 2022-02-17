"""Create post tables

Revision ID: 492c7326824c
Revises: 
Create Date: 2022-02-16 20:51:12.681418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '492c7326824c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)
                    )


def downgrade():
    op.drop_table('posts')
    pass
