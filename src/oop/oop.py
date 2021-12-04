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
    def calculate_total_price(self, x, y):
        return x * y


# creating the object based on the Item class
item1 = Item()
item1.name = "IPhone"
item1.price = 90
item1.quantity = 10
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "laptop"
item2.price = 50
item2.quantity = 20
print(item2.calculate_total_price(item2.price, item2.quantity))
