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
[link](https://www.w3schools.com/python/python_operators.asp)

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
