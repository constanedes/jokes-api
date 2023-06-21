from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///jokes.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
conn = engine.connect()
meta = MetaData()

