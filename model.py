from peewee import *

db = SqliteDatabase('local.db')

class BaseModel(Model):
    class Meta:
        database = db

class Transaccion(BaseModel):
    monto = IntegerField()
    descripcion = TextField()
    nombre = CharField(max_length=28)
    


