from sqlalchemy import create_engine ,inspect
from sqlalchemy import Table
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql+psycopg2://admin:admin@192.168.1.113:5432/target")


inspector = inspect(engine)
schemas = inspector.get_schema_names()

for schema in schemas:
    print("schema: %s" % schema)
    for table_name in inspector.get_table_names(schema=schema):
        for column in inspector.get_columns(table_name, schema=schema):
            print("Column: %s" % column)



