
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from src.static.config import config

connection_url = URL.create(
    config["MSSQL_LIB"],
    username=config["MSSQL_USER"],
    password=config["MSSQL_PASS"],
    host=config["MSSQL_HOST"],
    port=config["MSSQL_PORT"],
    database=config["MSSQL_DB"],
    query={
        "driver": config["MSSQL_DIRVER"],
    },
)

engine = create_engine(connection_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
