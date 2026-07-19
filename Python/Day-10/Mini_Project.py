'''
Student Report Card

Take input for:
Student Name
Physics Marks
Chemistry Marks
Maths Marks

Store the data in a dictionary.

Then display:
Student Name
All Marks
Total Marks
Percentage
Highest Marks
Lowest Marks

Use dictionary methods wherever possible.                                                                                                    '''

# CODE👇

# Taking input from the user
student = {
    "Student Name": input("Enter Student Name: "),
    "Physics": int(input("Enter Physics Marks: ")),
    "Chemistry": int(input("Enter Chemistry Marks: ")),
    "Maths": int(input("Enter Maths Marks: "))
}

# Store marks in a list
marks = [
    student["Physics"],
    student["Chemistry"],
    student["Maths"]
]

# Calculating total, percentage, highest and lowest marks
total = sum(marks)
percentage = (total / 300)*100
highest = max(marks)
lowest = min(marks)

# Displaying the report card
print("\n----- STUDENT REPORT CARD -----")
print("Student Name :", student["Student Name"])
print("Physics Marks :", student["Physics"])
print("Chemistry Marks :", student["Chemistry"])
print("Maths Marks :", student["Maths"])
print("Total Marks :", total)
print("Percentage :", round(percentage, 2))
print("Highest Marks :", highest)
print("Lowest Marks :", lowest)
print("--------------------------------")


''' Output:-
    Enter Student Name: Pratik Yadav
    Enter Physics Marks: 85
    Enter Chemistry Marks: 90
    Enter Maths Marks: 95

    ----- STUDENT REPORT CARD -----
    Student Name : Pratik Yadav
    Physics Marks : 85
    Chemistry Marks : 90
    Maths Marks : 95
    Total Marks : 270
    Percentage : 90.0
    Highest Marks : 95
    Lowest Marks : 85                                                                                                                         
    --------------------------------                                                                                                           '''