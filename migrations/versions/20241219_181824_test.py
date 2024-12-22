"""test

Revision ID: 9e845e396829
Revises: 71214442976e
Create Date: 2024-12-19 18:18:24.142205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e845e396829'
down_revision = '71214442976e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transcriptions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('text', sa.Text(), nullable=False))
        batch_op.drop_column('transcription')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transcriptions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('transcription', sa.TEXT(), nullable=False))
        batch_op.drop_column('text')

    # ### end Alembic commands ###