'''
 Topic :- Dictionary

✨ What is a Dictionary?
A dictionary stores data in key-value pairs.

Example:

CODE:-
student = {
    "name": "Pratik",
    "age": 20,
    "branch": "AIML"
}

✨ Access Values

CODE:-
print(student["name"])
print(student["age"])

Output:-
Pratik
20

✨ Add a New Item

student["city"] = "Bhopal"

✨ Update a Value

student["age"] = 21

✨ Remove an Item

student.pop("branch")

✨ Length of Dictionary

print(len(student))

✨ Print Keys

print(student.keys())

✨ Print Values

print(student.values())

✨ Print Both Keys and Values

print(student.items())

✨ Loop Through Dictionary

for key, value in student.items():
    print(key, ":", value)

✨ Check if Key Exists

if "name" in student:
    print("Key Found")

✨ Clear Dictionary

student.clear()

'''