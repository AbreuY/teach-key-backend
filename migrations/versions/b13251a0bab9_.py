"""empty message

Revision ID: b13251a0bab9
Revises: 911fcc98e1a0
Create Date: 2021-11-17 00:52:31.890790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b13251a0bab9'
down_revision = '911fcc98e1a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('professor', sa.Column('facebook', sa.String(length=250), nullable=True))
    op.add_column('professor', sa.Column('twitter', sa.String(length=250), nullable=True))
    op.add_column('professor', sa.Column('instagram', sa.String(length=250), nullable=True))
    op.add_column('professor', sa.Column('whatsapp', sa.String(length=250), nullable=True))
    op.drop_column('professor', 'contact_methods')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('professor', sa.Column('contact_methods', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('professor', 'whatsapp')
    op.drop_column('professor', 'instagram')
    op.drop_column('professor', 'twitter')
    op.drop_column('professor', 'facebook')
    # ### end Alembic commands ###
