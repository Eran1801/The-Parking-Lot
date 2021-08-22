from colorama import Fore

import data_services as svc
from data.dogs import Dogs
from data.owners import Owner
from infrastructure import state
from infrastructure.switchlang import switch


def run():
    while True:
        show_action()
        action = get_action()

        with switch(action) as action:
            action.case('l', log_in)
            action.case('c', create_account)
            action.case('b', book_cage)
            action.case('d', get_all_cages_details)
            action.case('e', exit())
            action.case('h', help_info)


def show_action():
    print('Which action would you like to take :')
    print('Press [L/l] to login to your account')
    print('Press [C/c] to create a user')
    print('Press [B/b] to book a cage to a dog')
    print('Press [D/d] to see all the dogs in the kennels')
    print('Press [E/e] to exit the app')
    print('Press [H/h] for help and info')
    print()


def log_in():
    email = input("Email address: ")
    password = input("Password: ")
    account = svc.find_account_by_email(email)

    if not account:
        error_msg("There is no account with this email please register")
        return
    if account.password is not password:
        error_msg("Incorrect password")
        return

    state.active_account = account
    success_msg(f"Login successful, welcome {account.name}")


def create_account():
    print('Hello! \n Welcome to The Barking Lot team \n Please register..\n')
    name = input('Full name:')
    email = input('Email address:').strip().lower()
    password = input('Password:')
    cell_phone = input('Cell-Phone:')
    age = int(input('Age:'))
    address = input('Address:')
    role = input('please press [e] for employee or [m] for manager:')

    #  We want to verify the account doesn't exist
    old_account = svc.find_account_by_email(email)
    if old_account:
        error_msg(f"ERROR: Account with email {email} already exists.")
        return

    #  svc.create_user return the Employee
    state.active_account = svc.create_user(name, email, password, cell_phone, age, address, role)
    success_msg(f"Account create successful with id :{state.active_account.id}")
    success_msg(f"Welcome aboard {name}")


def book_cage():
    if not state.active_account:
        error_msg("OOps, You must login first")
        return

    print('Lets add a new dog to the kennel')
    print('First we will need the information about the owner of the dog')

    owner = Owner()
    owner.owner_name = input('Name of the owner:')
    owner.owner_id = input('ID owner')
    owner.owner_cell_phone = input('cell-phone:')

    print('Now we take the information about the dog')
    number_of_dogs = int(input('How many dogs will stay in the kennel'))
    while number_of_dogs != 0:
        dog = Dogs()
        dog.dog_name = input("Name of the dog: ")
        dog.dog_id = input('Dog ID (zero of None)')
        dog.dog_species = input("Dog species: ")
        dog.dog_sex = input("Dog sex: ")
        dog.dog_age = int(input("Dog age: "))
        dog.check_in_date = input('Check-in date, d/m/Y: ')
        dog.check_out_date = input('Check-out date, d/m/Y: ')
        available_cages = svc.show_available_cages()
        print('Choose a cage number from the list below')
        print(available_cages)
        choose_cage_number = True
        while choose_cage_number:
            cage_number = int(input("Cage number: "))
            if cage_number not in available_cages:
                error_msg("This cage is taken, choose another one")
            else:
                dog.cage_number = cage_number
                choose_cage_number = False
                number_of_dogs -= 1
                owner.dogs_in_the_kennels.add(dog)
                dog.save()

    owner.save()


def get_all_cages_details():
    if not state.active_account:
        error_msg("OOps, You must login first")
        return

    for dog in Dogs.objects(
            cage_number__nin=0):  # To find any pages that don't have the tags coding use the $nin operator
        print(f'Dog name: {dog.dog_name} \n Cage number: {dog.cage_number} \n Check-out date: {dog.check_out_date}')


def help_info():
    email = 'TheBarkingLot@gmail.com'
    print(f"Hey there, for more information you can contact us throw our email address {email} \n")


def error_msg(text: str):
    print(Fore.LIGHTRED_EX + text)


def success_msg(text: str):
    print(Fore.LIGHTGREEN_EX + text)


def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()

    #  strip - Remove spaces at the beginning and at the end of the string:
    #  lower - lower() method takes no arguments and returns the lowercase string
