from orator import DatabaseManager, Schema, Model


DATABASES = {
    'sqlite': {
        'driver': 'sqlite',
        'database': 'local.db',
        'prefix': ''
    }
}

db = DatabaseManager(DATABASES)
Schema = Schema(db)
Model.set_connection_resolver(db)
