import uuid
class User(object):
    """docstring for User"""

    def __init__(self):
        pass


class Owners(User):
    def __init__(self,ownerName, item):
        self.ownerId=uuid.uuid1()
        self.ownerName=ownerName
        self.item = item
        
    
    stock_balance=[]
    items=[]


    def see_daily_sales(self):
        owner = User('Gloria', 'posho')
        item =StockItem('posho','500','1000','')
        items=items.append(item)
        daily_sales=[items]


    
        print (daily_sales)


    def see_stock_balances(self):
        item_stock_balance ={item:stock_balance}
        print (item_stock_balance)




class Managers(User):
    """docstring for Managers"""

    def __init__(self):
        pass


class Attendants(User):
    """docstring for Attendants"""

    def __init__(self):
        pass


store_owners=Owners('Gloria', 'posho')
store_owners.see_daily_sales()