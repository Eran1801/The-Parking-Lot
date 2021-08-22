from colorama import Fore
import data.mongo_setup as mongo_setup
from services import program_book


def main():
    mongo_setup.global_init()  # This function implemented in the "mongo_setup" file under data directory
    # And we only called her once and we need to it before we interact with anything else

    print_header()
    program_book.run()

    print("Hope to see you again, The Barking Lot")


def print_header():
    print(Fore.BLUE + '****************  The Barking Lot  ****************' + Fore.BLUE)
    print()
    print("Welcome to The Barking Lot!")
    print()


if __name__ == '__main__':
    main()
