"""Inicial

Revision ID: 56f9b475c92a
Revises: 
Create Date: 2021-09-11 12:38:54.044060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "56f9b475c92a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "units",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("initial", sa.String(length=10), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("initial"),
    )
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("unit_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["unit_id"],
            ["units.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "services",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("code", sa.String(length=15), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("unit", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["unit"],
            ["units.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "list_items",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("quantity", sa.Numeric(), nullable=False),
        sa.Column("items_list", sa.Integer(), nullable=False),
        sa.Column("service_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["items_list"],
            ["items.id"],
        ),
        sa.ForeignKeyConstraint(
            ["service_id"],
            ["services.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "list_services",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("quantity", sa.Numeric(), nullable=False),
        sa.Column("service_list", sa.Integer(), nullable=False),
        sa.Column("service_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["service_id"],
            ["services.id"],
        ),
        sa.ForeignKeyConstraint(
            ["service_list"],
            ["services.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("list_services")
    op.drop_table("list_items")
    op.drop_table("services")
    op.drop_table("items")
    op.drop_table("units")
    # ### end Alembic commands ###
