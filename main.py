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
    grandma_Rosa = Person.create(name="Rosa", birthday=date(1967, 12, 20), is_relative=False)
	grandma_Pepe = Person.create(name="Pepe", birthday=date(1967, 12, 20), is_relative=True)

    tommy_dog=Pet.create(owner=uncle_tomy,name="Fido",animal_type="Perro")
    ana_cat=Pet.create(owner=grandma_ana,name="Pelusa",animal_type="Gato")

    tommy_dog.name="Firulais"
    tommy_dog.save()

def get_family_members():
    for person in Person.select():
        print("Nombre :{} Cumpleano {}".format(person.name, person.birthday))


def get_family_member_birthday(name):
    family_member =Person.select().where(Person.name== name).get()
    print("{} cumple el : {}".format(name, family_member.birthday))

def delete_pet(nombre):
    query = Pet.delete().where(Pet.name== nombre)
    deleted_entries = query.execute()
    print("{} registros borrados".format(deleted_entries))


create_and_connect()
#create_family_members()
#get_family_members()
#get_family_member_birthday("Tommy")
delete_pet("Pelusa")
