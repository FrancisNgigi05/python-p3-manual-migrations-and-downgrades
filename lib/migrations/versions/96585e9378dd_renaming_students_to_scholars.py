"""Renaming students to scholars

Revision ID: 96585e9378dd
Revises: 791279dd0760
Create Date: 2024-04-05 15:22:16.846990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96585e9378dd'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')

def downgrade() -> None:
    op.rename_table('scholars', 'students')
