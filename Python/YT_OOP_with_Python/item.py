import csv

class Item():

    discount = 0.8
    all = []
    
    def __init__(self, name : str, price : float, quantity : int):
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        assert price >= 0, "Price should always be >= 0"
        assert quantity >= 0, "Quantity should always be >= 0"
        
        Item.all.append(self)
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def calculate_discounted_price(self):
        return self.price * self.discount
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    @classmethod
    def instantiate_using_csv(cls):
        with open("Python/YT_OOP_with_Python/data/product_prices.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_integer(num):
        
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False