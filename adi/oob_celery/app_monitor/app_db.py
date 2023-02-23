import databases
import pydantic

import ormar
import sqlalchemy

DATABASE_URL = 'postgresql://admin:admin@192.168.1.113:5432/target'

app_engine = sqlalchemy.create_engine(DATABASE_URL)


database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


# note that this step is optional -> all ormar cares is a internal
# class with name Meta and proper parameters, but this way you do not
# have to repeat the same parameters if you use only one database
class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
