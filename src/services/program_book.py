from colorama import Fore

import data_services as svc
from infrastructure import state
from infrastructure.switchlang import switch


def run():
    while True:
        show_action()
        action = get_action()

        with switch(action) as a:
            a.case('l', log_in)
            a.case('c', create_account)
            a.case('b', book_cage)


def show_action():
    print('Which action would you like to take :')
    print('Press [L/l] to login to your account')
    print('Press [C/c] to create an account')
    print('Press [B/b] to book a cage to a dog')
    print('Press [D/d] to see all the dogs in the kennels')
    print('Press [U/u] to see all the upcoming bookings')
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
    if not account.password is password:
        error_msg("Incorrect password")
        return

    state.active_account = account
    success_msg("Login successful")


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

    #  svc.create_account return the Employee
    state.active_account = svc.create_account(name, email, password, cell_phone, age, address, role)
    success_msg(f"Account create successful with id :{state.active_account.id}")


def book_cage():
    if not state.active_account:
        error_msg("OOps, You must login first")
        return

    dog_name = input("Name of the dog: ")
    dog_species = input("Dog species: ")
    dog_sex = input("Dog sex: ")
    dog_age = int(input("Dog age: "))
    cage_number = int(input("Cage number: "))


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
