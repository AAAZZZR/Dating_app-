"""Remove activities table and update references

Revision ID: 3c6f24533bc0
Revises: 6961d6ab2ef4
Create Date: 2024-09-30 19:13:14.237384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c6f24533bc0'
down_revision = '6961d6ab2ef4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activities', schema=None) as batch_op:
        batch_op.alter_column('host_id',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=32),
               existing_nullable=False)
        batch_op.drop_constraint('activities_host_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['host_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activities', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('activities_host_id_fkey', 'users', ['host_id'], ['username'])
        batch_op.alter_column('host_id',
               existing_type=sa.String(length=32),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    # ### end Alembic commands ###
