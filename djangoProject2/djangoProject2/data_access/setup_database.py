import sqlalchemy.engine
from sqlalchemy import create_engine
from django.apps import apps

localhoststr = "postgresql://postgres:Yipyapyop1@localhost:5432"
connection_string = localhoststr  # set this to the database string


def connect_to_database(connection_str: str):
    engine = create_engine(connection_str)
    engine.connect()
    print("connected to database")
    return engine


def get_engine() -> sqlalchemy.engine.Engine:
    config = apps.get_app_config("djangoProject2");
    return config.get_engine()
