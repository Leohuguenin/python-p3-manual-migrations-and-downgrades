"""Renaming students to scholars

Revision ID: 41d69aa38cae
Revises: 791279dd0760
Create Date: 2025-11-27 12:35:46.382854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41d69aa38cae'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')

