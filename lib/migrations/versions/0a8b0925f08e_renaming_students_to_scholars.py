"""Renaming students to scholars

Revision ID: 0a8b0925f08e
Revises: 791279dd0760
Create Date: 2023-09-07 22:54:03.544952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a8b0925f08e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    
