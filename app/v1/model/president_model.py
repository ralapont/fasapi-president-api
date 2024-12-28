import peewee

from app.v1.utils.db import db

class President(peewee.Model):
    id = peewee.AutoField()
    last_name = peewee.CharField()
    first_name = peewee.CharField()
    suffix = peewee.CharField(null=True)
    city = peewee.CharField()
    state = peewee.CharField()
    birth = peewee.DateField()
    death = peewee.DateField(null=True)

    class Meta:
        database = db
        db_table='president'