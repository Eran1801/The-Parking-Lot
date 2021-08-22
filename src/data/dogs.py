import mongoengine
from datetime import date  # will help me to show the registered_date in day/month/year


class Dogs(mongoengine.Document):
    registered_date = mongoengine.DateField(default=date.today().strftime("%d/%m/%Y"))
    dog_name = mongoengine.StringField(required=True)  # when required=true the user have to put in the species
    species = mongoengine.StringField(required=True)
    dog_sex = mongoengine.StringField(required=True)
    dog_age = mongoengine.FloatField(required=True)
    cage_number = mongoengine.IntField(required=True, unique=True)  # In which number of cage the god will stay

    meta = {

        'db_alias': 'core',
        'collection': 'dogs'

    }
