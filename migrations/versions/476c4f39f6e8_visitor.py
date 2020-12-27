"""visitor

Revision ID: 476c4f39f6e8
Revises: 
Create Date: 2020-12-27 18:57:07.731927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '476c4f39f6e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('unique_visitor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('visitor_id', sa.Integer(), nullable=True),
    sa.Column('visit_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('visitor_id', 'visit_date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('unique_visitor')
    # ### end Alembic commands ###
