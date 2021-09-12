from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
    Text,
    UniqueConstraint,
)

metadata = MetaData()

units = Table(
    "units",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50), nullable=False),
    Column("initial", String(10), nullable=False),
    UniqueConstraint("initial"),
)

feedstock = Table(
    "feedstock",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", Text, nullable=False),
    Column("unit_id", Integer, ForeignKey("units.id"), nullable=False),
    UniqueConstraint("name", "unit_id", name="feedstock_unique_constraint"),
)

compositions = Table(
    "compositions",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("code", String(15), nullable=False),
    Column("description", Text, nullable=False),
    Column("unit", Integer, ForeignKey("units.id"), nullable=False),
    UniqueConstraint("code"),
)

compositions_feedstock = Table(
    "compositions_feedstock",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("quantity", Numeric, nullable=False),
    Column("feedstock_id", Integer, ForeignKey("feedstock.id"), nullable=False),
    Column("composition_id", Integer, ForeignKey("compositions.id"), nullable=False),
)

compositions_services = Table(
    "compositions_services",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("quantity", Numeric, nullable=False),
    Column("service_id", Integer, ForeignKey("compositions.id"), nullable=False),
    Column("composition_id", Integer, ForeignKey("compositions.id"), nullable=False),
)
