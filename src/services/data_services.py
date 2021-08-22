from data.Employees import Employee
from data.cages import Cages


def create_user(name: str, email: str, password: str, cell_phone: str, age: int, address: str,
                role: str) -> Employee:
    employee = Employee()
    employee.name = name
    employee.email = email
    employee.password = password
    employee.cell_phone = cell_phone
    employee.age = age
    employee.address = address
    employee.role = role

    employee.save()

    return employee


def find_account_by_email(email: str) -> Employee:
    #  objects() - doc.mongoengine.org/guide/querying.html
    employee = Employee.objects(email=email).first()
    return employee


def find_cage_by_number(cage_number: int) -> Cages:
    cage = Cages.objects(cage_number=cage_number)
    return cage


def show_available_cages() -> list:
    available_cages = []
    for cage in Cages.objects(available=True):
        available_cages.insert(cage.cage_number, cage.cage_number)

    return available_cages
