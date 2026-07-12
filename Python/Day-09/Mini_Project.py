'''
Employee Database

Take input from user:
Employee Name
Employee ID
Department
Salary

Store them in a tuple and print:

----- Employee Details -----
Name :
ID :
Department :
Salary :                                                                                                                                   '''

# CODE👇
# Employee Database

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
salary = float(input("Enter Salary: "))

# Store data in a tuple
employee = (name, emp_id, department, salary)

# Display Employee Details
print("\n----- Employee Details -----")
print("Name       :", employee[0])
print("ID         :", employee[1])
print("Department :", employee[2])
print("Salary     :", employee[3])