# Python in one video

## hello world

### print

we can print any thing using the print keyword, like we have console.log() in js and in py we have print()

```py
print("hello world")
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
