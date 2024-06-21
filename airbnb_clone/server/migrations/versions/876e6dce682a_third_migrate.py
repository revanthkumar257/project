"""third migrate

Revision ID: 876e6dce682a
Revises: f8420c780b3b
Create Date: 2024-06-21 19:08:42.080569

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '876e6dce682a'
down_revision = 'f8420c780b3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('date_range', sa.String(length=255), nullable=False))
        batch_op.drop_column('details')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('details', mysql.VARCHAR(length=255), nullable=False))
        batch_op.drop_column('date_range')
        batch_op.drop_column('location')

    # ### end Alembic commands ###
