from django.apps import AppConfig
from djangoProject2.data_access.setup_database import connect_to_database, connection_string


class PostgresConfig(AppConfig):
    name = 'djangoProject2'
    verbose_name = "My Application"

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        self.engine = None

    def ready(self):
        self.engine = connect_to_database(connection_string)

    def get_engine(self):
        return self.engine
