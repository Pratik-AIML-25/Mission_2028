'''
Student Profile Formatter

Take input:
Full Name
Age
Department
College
Skills (comma separated)

Display them in a neat formatted profile and generate a username from the full name.                                                          '''


# CODE👇
full_name = input("Enter Full Name: ")
age = input("Enter Age: ")
department = input("Enter Department: ")
college = input("Enter College: ")
skills = input("Enter Skills (comma separated): ")

username = "".join(full_name.lower().split())

skills_list = [skill.strip() for skill in skills.split(",")]

print("\n----- STUDENT PROFILE -----")
print("Full Name :", full_name.title())
print("Age       :", age)
print("Department:", department)
print("College   :", college.title())
print("Username  :", username)
print("Skills    :", ", ".join(skills_list))


''' Output:-
    
    Example:
    Input: Enter Full Name: Pratik Yadav
           Enter Age: 20
           Enter Department: BTech(Hons.)CSE-AIML
           Enter College: SAGE University, Bhopal
           Enter Skills (comma separated): Python, C, C++, JAVA
           
    Output: 
    ----- STUDENT PROFILE -----
    Full Name : Pratik Yadav
    Age       : 20
    Department: BTech(Hons.)CSE-AIML
    College   : Sage University, Bhopal
    Username  : pratikyadav
    Skills    : Python, C, C++, JAVA                                                                                                          '''