"""create users table

Revision ID: be6c69c1a61a
Revises: 
Create Date: 2023-10-19 08:14:26.664619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be6c69c1a61a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String, unique=True, index=True),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('password', sa.String),
    )


def downgrade() -> None:
    op.drop_table('users')
