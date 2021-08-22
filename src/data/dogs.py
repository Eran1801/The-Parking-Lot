import mongoengine
from datetime import date  # will help me to show the registered_date in day/month/year


class Dogs(mongoengine.Document):
    registered_date = mongoengine.DateField(default=date.today().strftime("%d/%m/%Y"))
    dog_name = mongoengine.StringField(required=True)  # when required=true the user have to put in the species
    dog_id = mongoengine.StringField(unique=True)
    dog_species = mongoengine.StringField(required=True)
    dog_sex = mongoengine.StringField(required=True)
    dog_age = mongoengine.FloatField(required=True)
    cage_number = mongoengine.IntField(required=True, unique=True, default=0)  # In which number of cage the god will stay
    check_in_date = mongoengine.DateField(required=True)
    check_out_date = mongoengine.DateField(required=True)

    meta = {

        'db_alias': 'core',
        'collection': 'dogs'

    }
