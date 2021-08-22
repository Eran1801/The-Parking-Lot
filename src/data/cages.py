import mongoengine


class Cages(mongoengine.Document):  # basically says to mongoengine that this file is top level document
    cage_number = mongoengine.IntField(required=True, min_value=1, max_value=100, unique=True)  # i have only 100 cages in my kennels
    price = mongoengine.IntField(required=True)  # price for a night 18$
    available = mongoengine.BooleanField(required=True)

    meta = {

        'db_alias': 'core',
        'collection': 'cages'

    }
