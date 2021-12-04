# class
## create class


# class Item:
#     pass


# item1 = Item()
# item1.name = "IPhone"
# item1.price = 90000
# item1.quantity = 10

# Creating method under the class
class Item:
    def __init__(self, name, price, quantity):
        # print(f"An instace create: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x * y


# create the name,price,qtu using the constructor
item1 = Item("Iphone", 100, 5)
# prof
print(item1.name, item1.price, item1.quantity)
# item1.name = "IPhone"
# item1.price = 90
# item1.quantity = 10
# print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item("laptop", 50, 20)
# item2.name = "laptop"
# item2.price = 50
# item2.quantity = 20
# print(item2.calculate_total_price(item2.price, item2.quantity))
