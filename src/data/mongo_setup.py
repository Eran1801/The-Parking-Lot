import mongoengine

'''
This function ( global_init() ) gets more interested and complex with a a more complex in a real connections.
And we need to call this to MongoDB so we go the 'program' file in service

The more complex thing for example : 

data = dict(
        username=user_name_config_or_env,
        password=password_from_config_or_env,
        ....
        ....

mongoengine.register_connection(alias='core', name='snake_bnb' , **data)     

'''


def global_init():
    mongoengine.register_connection(alias="core", name="barking_lot", username=input("Enter your email"),
                                    password=input("Enter your password"))
