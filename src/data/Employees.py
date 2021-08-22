import mongoengine


class Employee(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True, unique=True)
    password = mongoengine.StringField(required=True)
    cell_phone = mongoengine.StringField(required=True)
    age = mongoengine.IntField(required=True)
    address = mongoengine.StringField()
    role = mongoengine.StringField(required=True)

    mete = {

        'db_alias': 'core',
        'collection': 'employee'

    }
