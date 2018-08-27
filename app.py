class User(object):
    """docstring for User"""

    def __init__(self):
        pass


class Owners(User):
    def __init__(self,ownerId,ownerName):
        self.ownerId=ownerId
        self.ownerName=ownerName

    def see_daily_sales(self):
        pass

    def see_stock_balances(self):
        pass


class Managers(User):
    """docstring for Managers"""

    def __init__(self):
        pass


class Attendants(User):
    """docstring for Attendants"""

    def __init__(self):
        pass
