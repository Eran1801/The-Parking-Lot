import mongoengine


# Here we need to tell mongoengine that this file is EmbeddedDocument,means that have a connection with another document
class Booking(mongoengine.EmbeddedDocument):
    guest_owner_id = mongoengine.ObjectIdField(unique=True,required=True)
    guest_dog_id = mongoengine.ObjectIdField(unique=True)  # His chip number

    booked_date = mongoengine.DateTimeField()
    check_in_date = mongoengine.DateTimeField(required=True)
    check_out_date = mongoengine.DateTimeField(required=True)

    review = mongoengine.StringField(max_length=500)




