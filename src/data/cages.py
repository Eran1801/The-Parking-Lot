import mongoengine
from data.bookings import Booking


class Cages(mongoengine.Document):  # basically says to mongoengine that this file is top level document
    cage_number = mongoengine.IntField(required=True, min_value=1, max_value=100, unique=True)  # i have only 100 cages in my kennels
    big_dog_fit = mongoengine.BooleanField(required=True)  # for example cage number 5 is the only cage available but it to small for him
    price = mongoengine.IntField(required=True)  # price for a night, big dog = 18$ big dog = 23$

    bookings = mongoengine.EmbeddedDocumentListField(Booking)

    meta = {

        'db_alias': 'core',
        'collection': 'cages'

    }
