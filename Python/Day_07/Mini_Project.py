'''
Student Result using Functions

Take input:
Name
Physics
Chemistry
Maths

Function should:
Calculate Total
Calculate Percentage
Return Grade

Example:-
Enter Name: Pratik
Physics: 90
Chemistry: 95
Maths: 80

Name : Pratik
Total : 265
Percentage : 88.33%
Grade : A                                                                                                                                '''


# CODE

# Function to calculate total marks
def calculate_total(physics, chemistry, maths):
    return physics + chemistry + maths

# Function to calculate percentage
def calculate_percentage(total):
    return (total / 300) * 100

# Function to return grade
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

# Main Program
name = input("Enter Name: ")

physics = int(input("Enter Physics Marks: "))
chemistry = int(input("Enter Chemistry Marks: "))
maths = int(input("Enter Maths Marks: "))

# Function Calls
total = calculate_total(physics, chemistry, maths)
percentage = calculate_percentage(total)
grade = get_grade(percentage)

# Output
print("\n----- Student Result -----")
print("Name       :", name)
print("Total      :", total)
print("Percentage : {:.2f}%".format(percentage))
print("Grade      :", grade)