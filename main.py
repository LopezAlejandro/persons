from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database



def create_and_connect():
    db.connect()
    db.create_tables([Person,Pet])

def create_family_members():
    uncle_tomy = Person(name="Tommy",birthday=date(2000,11,11),is_relative=True)
    uncle_tomy.save()

    grandma_ana = Person.create(name="Ana",birthday=date(1967,12,20),is_relative=False)

create_and_connect()
create_family_members()
