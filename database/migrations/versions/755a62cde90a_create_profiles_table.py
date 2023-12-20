"""create_profiles_table

Revision ID: 755a62cde90a
Revises: be6c69c1a61a
Create Date: 2023-12-20 15:04:23.833092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '755a62cde90a'
down_revision = 'be6c69c1a61a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "profiles",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("user_id", sa.Integer, unique=True, index=True),
        sa.Column("firstname", sa.String(100)),
        sa.Column("lastname", sa.String(100)),
        sa.Column("middlename", sa.String(100)),
        sa.Column("mobile", sa.String(100)),
        sa.Column("age", sa.Integer),
        sa.Column("gender", sa.Integer),
        sa.Column("civil_status", sa.Integer),
        sa.Column("notification_type", sa.Integer),
        sa.Column("birthdate", sa.Date),
        sa.Column("address", sa.Text),
        sa.Column("created_at", sa.DateTime, default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime, default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("profiles")