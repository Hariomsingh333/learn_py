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

## Constructor

we can make the Constructor using the very unique name double underscore init double underscore

```py
# name
__init__
```

basically constructor is a method with a unique name that you need to call it the way it in intentionally in order to use its special futures.

<br>

Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python double_underscore init double_underscore() the method is called the constructor and is always called when an object is created.

#### syntax

```py
class Item:
    def __init__(self):
        #body of the constructor
```

```py
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
# item1.name = "IPhone"
# item1.price = 90
# item1.quantity = 10
print(item1.calculate_total_price(item1.price, item1.quantity))

```
