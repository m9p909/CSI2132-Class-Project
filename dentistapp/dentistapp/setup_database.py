import sqlalchemy.engine
from sqlalchemy import create_engine
from django.apps import apps
import environ

env = environ.Env()
env.read_env()
localhoststr = "postgresql://postgres:Yipyapyop1@localhost:5432"
victorhoststr = "postgresql://postgres:3574128960%40Az@localhost:5432/CSI2132_DB"
connection_string = env("DATABASE_STR")  # set this to the database string


def connect_to_database(connection_str: str):
    engine = create_engine(connection_str)
    engine.connect()
    print("connected to database")
    return engine


def get_engine() -> sqlalchemy.engine.Engine:
    config = apps.get_app_config("dentistapp");
    return config.get_engine()
