# Python in one video

## hello world

### print

we can print any thing using the print keyword, like we have console.log() in js and in py we have print()

```py
print("hello world")
```

we can also print using the variable and string together

```python
dob = input("enter your DOB: ")
int_dob = int(dob)
sum = 2021 - int_dob
# using the f and {your_variable_name}
print(f"your age is {sum}")
```

#### fun fact

python always use **snake_case**

```py
first_name = "john"
```

## Variable

we don't need to define the data type before type a variable because python is a dynamic type language. so don't need to define the data type

just write the variable name and value

```python
name = "hari om singh"
```

## Receiving input

so how to receiving input using python, so in python we have another build in feature called **input**,
<br>
we can use the input method to take input from user

```py
your_name = input("enter your name: ")
print("hey! " + your_name)
```

## Type Conversion

in python we can not add a int to str,

```py
your_dob = input("enter your dob: ")
age = 2021 - your_dob
print(age)
```

this code give us error, and the error say that you can't add the str to an int

<br>

so we need to convert the str to int, and python has an int() method to convert into int

```py
your_dob = input("enter your dob: ")
age = 2021 - int(your_dob)
print(age)
```

## String

the string is a sequence of Unicode characters written inside a single or double-quote
<br>
we can write string in double-quote

```python
# string
str = "hello world"
```

in python we have so many string method

- upper()
- lower()
- replace()
- capitalize()
- count()
- replace()
- find()

all method not change our original string, all just return a new string

```python
str = "hello world")
print(str.upper()) # HELLO WORLD
```

## Operators

in python have many operator

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

all operator cover in this like or search in google
[link]("https://www.w3schools.com/python/python_operators.asp")

## Conditional Statement (if/else)

so we use conditional statement to make decision.

```python
age = int(input("enter you age: "))
if age >= 18:
    print(f"you are aviable to vote, your age is {age}")
else:
    print(f"you are not aviable to vote :(, your age is {age}")
```

or

```python
temperature = 25
if temperature >= 30:
    print(f"it's a hot day and the temp is {temperature}")
elif temperature >= 20 and temperature <= 30:
    print(f"it's a normal day temp: {temperature}")
elif temperature < 20:
    print(f"it's a cold day")
else:
    print("no data found 404")

```

## Loops

Python has two primitive loop commands:

- while loops
- for loops

### while loop

we use while loop to repeat a block of code multiple times
<br>
if the while loop condition is true then the while loop run

ex- print 1 to 5

```py
while num <= 5:
    print(num)
    num = num + 1
```

```py
# loop list using while loop
num = [1, 2, 3, 4, 5]
i = 0
while i < len(num):
    print(num[i])
    i = i + 1
```

### for loop

```py
# for loop
num = [1, 2, 3, 4, 5]
for i in num:
    print(i)
```

## Lists

basically list meaning array

```py
name = ["sonu", "monu", "hari", "shivam", "john", "serten"]
print(name)
print(name[2])
```

### List method

list have also bunch of method like we have in string

```py
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num.append(11) # to add in -1 index
num.insert(2, 45) # add in middle or type the index and add number
num.remove(3) # remove the list using the index
num.clear() # it's clear all the list

print(1 in num) # True , it mean is 1 in there we use the in keyword
```
