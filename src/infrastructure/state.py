from typing import Optional

from data.Employees import Employee
import services.data_services as svc

# If an explicit value of None is allowed, the use of Optional is appropriate, whether the argument is optional or not
active_account: Optional[Employee] = None  # inside the [] we put the variable type


def reload_account():
    global active_account
    if not active_account:
        return

    active_account = svc.find_account_by_email(active_account.email)
