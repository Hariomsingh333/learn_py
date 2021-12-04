# Date: 04 / 12 / 2021

# Object Oriented Programming with Python

In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.(geeksforgeeks)

## Main Concepts of Object-Oriented Programming (OOPs)

- Class
- Objects
- Polymorphism
- Encapsulation
- Inheritance

### Class

A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods.

- here we use the pass keyword for default creating example of object

```py
class Item:
    pass

# creating object using the Item class
item1 = Item()
item1.name = "IPhone"
item1.price = 90000
item1.quantity = 10
```

#### create method under class

when we create method in python we need to specify a argument called _self_, then we are able to create a method in classes

```py
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
```
