from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

jokes = Table(
    "jokes",
    meta,
    Column(
        "id",
        Integer,
        primary_key=True,
        nullable=False,
        comment="Unique autoincremental Id",
    ),
    Column("title", String(255), nullable=False, comment="First question for the joke"),
    Column(
        "punchline",
        String(255),
        nullable=False,
        comment="The joke punchline, if not have put a dot char",
    ),
)

meta.create_all(engine)
