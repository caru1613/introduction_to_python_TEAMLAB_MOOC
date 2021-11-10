class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items
        
    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("New item added")
        else:
            raise ValueError("Invalid item")
    def get_number_of_items(self):
        return len(self.__items)

my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
print(my_inventory.get_number_of_items())

items = my_inventory.items
items.append(Product())

print(my_inventory.get_number_of_items())