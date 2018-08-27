import time
import uuid


class StockItem():
    """docstring for StockItem"""

    def __init__(self, name, purchase_price, sale_price):
        self.id = uuid.uuid1()
        self.name = name
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.timestamp = time.time()

    def item_added(self):
        '''adds item '''
        pass

    def update_stock_balance(self):
        '''update the stock balance'''
        pass


class User(StockItem):
    """docstring for User"""

    def __init__(self, username, role, userid, password):
        self.username = username
        self.role = role
        self.userid = uuid.uuid1()
        self.password = password
        self.timestamp = time.time()

    def login(self, username, password):
        if username == self.username and password == self.password:
            print('username is logged in')

    def logout(self):
        print('User logged out')


class Owners(User):
    """docstring for Owners"""

    def __init__(self):
        pass


class Managers(User):
    """docstring for Managers"""

    def __init__(self):
        pass


class Attendants(User):
    """docstring for Attendants"""

    def __init__(self):
        pass


def print_menu():  # Your menu design here
    print(30 * "-", "MENU", 30 * "-")
    print("1. User as Owner")
    print("2. Menu as Manager")
    print("3. Menu as Attendant")
    print("4. Exit")
    print(67 * "-")


loop = True

while loop:  # While loop which will keep going until loop = False
    print_menu()  # Displays menu
    choice = int(input("Enter your choice [1-4]: "))

    if choice == 1:
        print("Menu 1 has been selected")
        owner = Owners()
        # You can add your code or functions here
    elif choice == 2:
        print("Menu 2 has been selected")
        Manager = Managers()
        # You can add your code or functions here
    elif choice == 3:
        print("Menu 3 has been selected")
        Attendant = Attendants()
        # You can add your code or functions here
    elif choice == 4:
        print("Menu 4 has been selected")
        # You can add your code or functions here
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selection. Enter any key to try again..")


print_menu()
