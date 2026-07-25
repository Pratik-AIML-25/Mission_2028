'''
TOPIC :- Advanced Strings

✨strip()
Removes extra spaces from the beginning and end of a string.

text = "   Python   "
print(text.strip())

Output
Python

✨ lstrip()
Removes spaces only from the left side.

text = "   Python"
print(text.lstrip())

Output
Python

✨ rstrip()
Removes spaces only from the right side.

text = "Python   "
print(text.rstrip())

Output

Python

✨ split()
Splits a string into a list.

name = "Pratik Yadav"
print(name.split())

Output
['Pratik', 'Yadav']

✨ join()
Joins list elements into one string.

words = ["Python", "is", "Easy"]
print(" ".join(words))

Output
Python is Easy

✨ find()
Returns the first index of a character.

text = "Python"
print(text.find("h"))

Output
3

If the character is not found:

print(text.find("z"))

Output
-1
✨ index()
Works like find(), but gives an error if the character is not found.

text = "Python"
print(text.index("h"))

Output
3

✨ replace()

text = "I Love Java"
print(text.replace("Java", "Python"))

Output
I Love Python

✨ isalpha()
Checks whether all characters are alphabets.

print("Python".isalpha())
print("Python123".isalpha())

Output
True
False
✨ isalnum()
Checks whether a string contains only letters and numbers.

print("Python123".isalnum())
print("Python@123".isalnum())

Output
True
False

✨ islower()

print("python".islower())

Output
True
✨ isupper()

print("PYTHON".isupper())

Output
True

✨ capitalize()

text = "python programming"
print(text.capitalize())

Output
Python programming

✨ swapcase()

text = "Python123"
print(text.swapcase())

Output
pYTHON123

✨ String Formatting (f-string)

name = "Pratik"
age = 20

print(f"My name is {name} and I am {age} years old.")

Output
My name is Pratik and I am 20 years old.

✨ Summary of Methods

Method	                     Purpose

strip()	              Remove spaces from both sides
lstrip()	          Remove left spaces
rstrip()	          Remove right spaces
split()	              Convert string into list
join()	              Convert list into string
find()	              Find index (returns -1 if not found)
index()	              Find index (gives error if not found)
replace()	          Replace text
isalpha()	          Check only letters
isalnum()	          Check letters and numbers
islower()	          Check lowercase
isupper()	          Check uppercase
capitalize()	      Capitalize first letter
swapcase()	          Toggle case
f""	                  Format strings

'''