"""add language to races

Revision ID: 89a8b1b7189f
Revises: a1f49c875808
Create Date: 2018-08-27 19:37:09.525655+02:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89a8b1b7189f'
down_revision = 'a1f49c875808'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('race_languages',
    sa.Column('race_id', sa.Integer(), nullable=False),
    sa.Column('language_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['language_id'], ['languages.id'], name=op.f('fk_race_languages_language_id_languages')),
    sa.ForeignKeyConstraint(['race_id'], ['races.id'], name=op.f('fk_race_languages_race_id_races')),
    sa.PrimaryKeyConstraint('race_id', 'language_id', name=op.f('pk_race_languages'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('race_languages')
    # ### end Alembic commands ###