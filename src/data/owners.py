import mongoengine
from datetime import date


#  The owner of the dog
class Owner(mongoengine.Document):
    owner_name = mongoengine.StringField(required=True)
    owner_cell_phone = mongoengine.StringField(required=True)

    dogs_in_the_kennels = set()

    meta = {

        'db_alias': 'core',
        'collection': 'owners'

    }
