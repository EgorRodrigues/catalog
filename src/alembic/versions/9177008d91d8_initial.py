"""Initial

Revision ID: 9177008d91d8
Revises: 
Create Date: 2021-09-22 14:24:35.749157

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "9177008d91d8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "units",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("slug", sa.String(length=10), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_table(
        "compositions",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("code", sa.String(length=15), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("unit", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["unit"],
            ["units.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
    )
    op.create_table(
        "feedstock",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("unit_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["unit_id"],
            ["units.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "description", "unit_id", name="feedstock_unique_constraint"
        ),
    )
    op.create_table(
        "compositions_feedstock",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("quantity", sa.Numeric(), nullable=False),
        sa.Column("feedstock_id", sa.Integer(), nullable=False),
        sa.Column("composition_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["composition_id"],
            ["compositions.id"],
        ),
        sa.ForeignKeyConstraint(
            ["feedstock_id"],
            ["feedstock.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "compositions_services",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("quantity", sa.Numeric(), nullable=False),
        sa.Column("service_id", sa.Integer(), nullable=False),
        sa.Column("composition_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["composition_id"],
            ["compositions.id"],
        ),
        sa.ForeignKeyConstraint(
            ["service_id"],
            ["compositions.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "prices",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("date_create", sa.DateTime(), nullable=False),
        sa.Column("price", sa.Numeric(), nullable=False),
        sa.Column("feedstock_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["feedstock_id"],
            ["feedstock.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("prices")
    op.drop_table("compositions_services")
    op.drop_table("compositions_feedstock")
    op.drop_table("feedstock")
    op.drop_table("compositions")
    op.drop_table("units")
    # ### end Alembic commands ###