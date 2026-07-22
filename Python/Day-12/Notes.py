'''
TOPIC :- Strings

✨ What is a String?
1) A string is a sequence of characters enclosed in quotes.
2) Strings are immutable (cannot be changed after creation).

name = "Pratik"
city = 'Bhopal'

✨ String Indexing

name = "Python"

print(name[0])   # P
print(name[1])   # y
print(name[-1])  # n

✨ String Slicing

name = "Python"

print(name[0:3])   # Pyt
print(name[2:6])   # thon
print(name[:4])    # Pyth
print(name[::-1])  # nohtyP

✨ Useful String Methods

upper()
lower()
title()
capitalize()
strip()
replace()
find()
count()
startswith()
endswith()

Examples:

name = "pratik yadav"

print(name.upper())
print(name.title())
print(name.count("a"))

✨ Checking Methods

isalnum()
isalpha()
isdigit()
isspace()
islower()
isupper()

✨ Joining Strings

first_name = "Pratik"
last_name = "Yadav"

print(first_name + " " + last_name)

✨ String Formatting

name = "Pratik"
age = 20

print(f"My name is {name} and I am {age} years old.")

'''