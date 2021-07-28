from orator import DatabaseManager, Schema, Model


DATABASES = {
    'sqlite': {
        'driver': 'sqlite',
        'database': 'local.db',
        'prefix': '',
        # 'foreign_keys': True,
        'log_queries': True
    }
}

db = DatabaseManager(DATABASES)
Schema = Schema(db)
Model.set_connection_resolver(db)
