"""add_owner_id_post_table

Revision ID: c8e80330fe40
Revises: b0733917bc41
Create Date: 2022-02-16 22:49:29.884675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8e80330fe40'
down_revision = 'b0733917bc41'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint(constraint_name='post_users_fk', table_name='posts')
    op.drop_column(table_name='posts', column_name='owner_id')
    pass
