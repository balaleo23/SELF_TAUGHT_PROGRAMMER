class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []
    
    def purchase(self,inventory,product):
        inventory_dict =inventory.inventory
        # self.inventory = inventory_dict
        # self.product = product
        if product in inventory_dict:
            if inventory_dict[product]>0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print("we are out of stocks")
        else:
            print("we dont have product")
    
    def print_purchases(self):
        for item in self.purchases:
            print(item)


class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price


class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self,product,quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product] += quantity


    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key +":"+str(value))



customer_1= Customer("jji","jo@gmail.com")
product_1 = Product("cell",250)


inventor = Inventory()
inventor.add_product("apple",250)
inventor.add_product("iphone",100)



inventor.print_inventory()
customer_1.purchase(inventor,"apple")
inventor.print_inventory()