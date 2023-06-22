from sqlalchemy import create_engine
from sqlalchemy.orm import Session

SQL_DATABASE_URL = "sqlite:///jokes.db"
engine = create_engine(
    SQL_DATABASE_URL, connect_args = {"check_same_thread": False}
)


