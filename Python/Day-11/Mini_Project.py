'''
Student Club Registration System

Take input from the user:

- Name
- Department
- 5 Skills

Store the skills in a set.

Display:

----- STUDENT CLUB DETAILS -----

Name :
Department :
Skills :

1.
2.
3.
...

Total Unique Skills :

--------------------------------
Example
Enter Name: Pratik Yadav
Enter Department: AIML

Enter 5 Skills:
Python
Git
Python
Machine Learning
Communication

----- STUDENT CLUB DETAILS -----

Name : Pratik Yadav
Department : AIML

Skills:
- Python
- Git
- Machine Learning
- Communication
- Team Leadership

Total Unique Skills : 5

--------------------------------                                                                                                             '''

# CODE👇

# Taking input from the user
name = input("Enter Name: ")
department = input("Enter Department: ")

# Creating an empty set for skills
skills = set()

print("\nEnter 5 Skills:")
for i in range(5):
    skill = input()
    skills.add(skill)

# Displaying the details
print("\n----- STUDENT CLUB DETAILS -----")

print("\nName :", name)
print("Department :", department)

print("\nSkills:")
for skill in sorted(skills):
    print("-", skill)

print("\nTotal Unique Skills :", len(skills))

print("\n--------------------------------")


''' Output:-
    Enter Name: Pratik Yadav
    Enter Department: AIML

    Enter 5 Skills:
    Python
    Git
    Machine Learning
    Communication
    Team Leadership

    ----- STUDENT CLUB DETAILS -----

    Name : Pratik Yadav
    Department : AIML

    Skills:
    - Communication
    - Git
    - Machine Learning
    - Python
    - Team Leadership

    Total Unique Skills : 5

    --------------------------------                                                                                                         '''