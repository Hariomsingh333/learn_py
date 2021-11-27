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
"""
temperature = 25
if temperature >= 30:
    print(f"it's a hot day and the temp is {temperature}")
elif temperature >= 20 and temperature <= 30:
    print(f"it's a normal day temp: {temperature}")
elif temperature < 20:
    print(f"it's a cold day")
else:
    print("no data found 404")
