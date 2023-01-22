from sqlalchemy import create_engine, Table, MetaData
from os import getenv

def get_connection_url():
    DATABASE_HOST = getenv("DATABASE_HOST")
    DATABASE_PORT = getenv("DATABASE_PORT")
    DATABASE_USER = getenv("DATABASE_USER")
    DATABASE_PASSWORD = getenv("DATABASE_PASSWORD")
    DATABASE_NAME = getenv("DATABASE_NAME")
    return f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

def create_tables(app, db):
    with app.app_context():
        db.create_all()

def get_connection():
    conn = create_engine(get_connection_url())
    metaData = MetaData()
    connection = conn.connect()
    
    distribution_table = Table("user_distribution", metaData, autoload_with=conn, autoload=True)
    genre_table = Table("genre", metaData, autoload_with=conn, autoload=True)
    
    return {"connection": connection, "distribution_table": distribution_table, "genre_table": genre_table}
