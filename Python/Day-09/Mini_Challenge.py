'''
Student Information

Create a tuple:
(Name, Age, City)

Output
Name :
Age :
City :

Example
Name : Pratik
Age : 20
City : Bhopal                                                                                                                               '''

# CODE👇
name = input("Enter Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")

student = (name, age, city)

print("\nStudent Information")
print("Name :", student[0])
print("Age  :", student[1])
print("City :", student[2])