"""empty message

Revision ID: c3e54619fe20
Revises: a391670e4845
Create Date: 2020-06-27 16:02:24.546334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3e54619fe20'
down_revision = 'a391670e4845'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_genres',
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_genres')
    # ### end Alembic commands ###
