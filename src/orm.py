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

items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", Text, nullable=False),
    Column("unit_id", Integer, ForeignKey("units.id"), nullable=False),
)

services = Table(
    "services",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("code", String(15), nullable=False),
    Column("description", Text, nullable=False),
    Column("unit", Integer, ForeignKey("units.id"), nullable=False),
    UniqueConstraint("code")
)

list_items = Table(
    "list_items",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("quantity", Numeric, nullable=False),
    Column("items_list", Integer, ForeignKey("items.id"), nullable=False),
    Column("service_id", Integer, ForeignKey("services.id"), nullable=False),
)

list_services = Table(
    "list_services",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("quantity", Numeric, nullable=False),
    Column("service_list", Integer, ForeignKey("services.id"), nullable=False),
    Column("service_id", Integer, ForeignKey("services.id"), nullable=False),
)
