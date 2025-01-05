from peewee import *
from .president_model import President

from app.v1.utils.db import db

class Picture(Model):
    pict_id =  ForeignKeyField(President, primary_key=True)
    pict_icon = CharField()
    pict_data = CharField()

    class Meta:
        database = db
        db_table='picture'