# variable

"""
name = "hari om singh"
print(name)

price = 99.99
print(price)

first_name = "john"
print(first_name)

name = "John Smith"
age = 20
new_patient = True
"""


# Receiving input
"""
your_name = input("enter your name: ")
print("hey! " + your_name)
"""
## Type Conversion
"""
your_dob = input("enter your dob: ")
age = 2021 - int(your_dob)
print(age)

first = input("First: ")
second = input("Second: ")
sum = float(first) + int(second)
print(sum)

dob = input("enter your DOB: ")
int_dob = int(dob)
sum = 2021 - int_dob
print(f"your age is {sum}")

"""
## String

"""
str = "hello world"
print(str.upper())
print(str.lower())
print(str.find("w"))
print(str.replace("world", "hari"))
"""
# Conditional Statement (if/else)
"""
age = int(input("enter you age: "))
if age >= 18:
    print(f"you are aviable to vote, your age is {age}")
else:
    print(f"you are not aviable to vote :(, your age is {age}")


temperature = 25
if temperature >= 30:
    print(f"it's a hot day and the temp is {temperature}")
elif temperature >= 20 and temperature <= 30:
    print(f"it's a normal day temp: {temperature}")
elif temperature < 20:
    print(f"it's a cold day")
else:
    print("no data found 404")
"""
# challenge
# cover pound to kg
"""
weight = int(input("enter you weight: "))
which = input("for pound write P or kg then write K: ")
if which == "P":
    sum = weight * 0.45359237
    print(f"{sum} kg")
if which == "K":
    print(f"{weight} Kg")
"""

# Loops

# while loop
"""
num = 1
# when the while condition is true then the while loop run
while num <= 5:
    print(num)
    num = num + 1


i = 1
while i <= 10:
    print(i * "*")
    i = i + 1
"""

# loop list using while loop
"""
num = [1, 2, 3, 4, 5]
i = 0
while i < len(num):
    print(num[i])
    i = i + 1
"""
# for loop
"""
num = [1, 2, 3, 4, 5]
for i in num:
    print(i)
"""
# List
"""
name = ["sonu", "monu", "hari", "shivam", "john", "serten"]
print(name)
print(name[2])

# list method
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num.append(11)  # to add in -1 index
num.insert(2, 45)  # add in middle or type the index and add number
num.remove(3)  # remove the list using the index
num.clear()  # it's clear all the list

"""

# function
"""
def say_hi(str):
    print(f"hey {str}")


say_hi("hari")
"""
# Tuples
"""
the_tuples = ("bus", "car", "bike")
print(the_tuples)
"""
