class User(object):
    """docstring for User"""

    def __init__(self):
        pass


class Owners(User):
    def __init__(self,ownerId,ownerName):
        self.ownerId=uuid.uuid1()
        self.ownerName=ownerName

    def see_daily_sales(self):
        self.daily_sales=daily_sales
        print (daily_sales)


    def see_stock_balances(self):
        item = item

        stock_balance= stock_balance
        item_stock_balance ={item:stock_balance}
        print (item_stock_balance)

store_owners=[]


class Managers(User):
    """docstring for Managers"""

    def __init__(self):
        pass


class Attendants(User):
    """docstring for Attendants"""

    def __init__(self):
        pass
