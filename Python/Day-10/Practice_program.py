# Program-1 :- Create a dictionary containing your name, age, and city. Print the dictionary.

# CODE👇
student = {
    "name" : "Pratik Yadav",
    "age" : 20,
    "city" : "Bhopal"
}
print(student)


# Program-2 :- Print only your name from the dictionary.

# CODE👇
student = {
    "name" : "Pratik Yadav",
    "age" : 20,
    "city" : "Bhopal"
}
print(student["name"])


# Program-3 :- Add a new key called branch.

# CODE👇
student = {
    "name" : "Pratik Yadav",
    "age" : 20,
    "city" : "Bhopal"
}
student ["branch"] = "AIML"
print(student)


# Program-4 :- Update your age.

# CODE👇
student = {
    "name" : "Pratik Yadav",
    "age" : 20,
    "city" : "Bhopal"
}
student["age"] = 21
print(student)


# Program-5 :- Print the total number of key-value pairs.

# CODE👇
student = {
    "name" : "Pratik Yadav",
    "age" : 20,
    "city" : "Bhopal"
}
print(len(student))


# Program-6 :- Print all the keys.

# CODE👇
student = {
    "name" : "Pratik Yadav",
    "age" : 20,
    "city" : "Bhopal"
}
print(student.keys())


# Program-7 :- Print all the values.

# CODE👇
student = {
    "name" : "Pratik Yadav",
    "age" : 20,
    "city" : "Bhopal"
}
print(student.values())


# Program-8 :- Print all key-value pairs using items().

# CODE👇
student = {
    "name" : "Pratik Yadav",
    "age" : 20,
    "city" : "Bhopal"
}
print(student.items())


# Program-9 :- Remove the city key using pop().

# CODE👇
student = {
    "name" : "Pratik Yadav",
    "age" : 20,
    "city" : "Bhopal"
}
student.pop("city")
print(student)


# Program-10 :- Check whether the key "age" exists.

# CODE👇
student = {
    "name" : "Pratik Yadav",
    "age" : 20,
    "city" : "Bhopal"
}
if "age" in student:
    print("Key Found")


# Program-11 :- Print the dictionary using a for loop.

# CODE👇
student = {
    "name" : "Pratik Yadav",
    "age" : 20,
    "city" : "Bhopal"
}
for key, value in student.items():
    print(key, ":", value)


# Program-12 :- Create a dictionary of 5 subjects with their marks and print all subjects with marks.

# CODE👇
marks = {
    "Maths": 88,
    "Physics": 92,
    "Chemistry": 85,
    "English": 90,
    "Computer Science": 95
}
for subject, mark in marks.items():
    print(subject, ":", mark)


# Program-13 :- Find the highest marks from the dictionary values.

# CODE👇
marks = {
    "Maths": 88,
    "Physics": 92,
    "Chemistry": 85,
    "English": 90,
    "Computer Science": 95
}
highest_marks = max(marks.values())       # Finding the highest marks
print("Highest Marks =", highest_marks)   # Printing the highest marks

# Program-14 :- Find the lowest marks from the dictionary values.

# CODE👇
marks = {
    "Maths": 88,
    "Physics": 92,
    "Chemistry": 85,
    "English": 90,
    "Computer Science": 95
}
lowest_marks = min(marks.values())      # Finding the lowest marks
print("Lowest Marks =", lowest_marks)   # Printing the lowest marks


# Program-15 :- Clear the dictionary and print it.

# CODE👇
marks = {
    "Maths": 88,
    "Physics": 92,
    "Chemistry": 85,
    "English": 90,
    "Computer Science": 95
}
marks.clear()                                  # Clearing the dictionary
print("Dictionary after clearing:", marks)     # Printing the empty dictionary