# Program-1 :- Input Name

name = input("Enter your Name : ")
print(name)


# Program-2 :- Input Age

age = input("Enter the Age : ")
print(age)


# Program-3 :- Add two Numbers

a = int(input("First Number: "))
b = int(input("Second Number: "))
print("Sum =", a + b)


# Program-4 :- Subtract two Numbers

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print("Difference =", a - b)


# Program-5 :- Multiply two Numbers

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print("Product =", a * b)


# Program-6 :- Divide two Numbers

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("Division =", a / b)


# Program-7 :- Square of Numbers

num = int(input("Enter Number: "))
print("Square =", num * num)


# Program-8 :- Area Of Rectangle

length = float(input("Length: "))
breadth = float(input("Breadth: "))

print("Area =", length * breadth)

# Program-9 :- Swap two numbers

a = int(input("Enter A: "))
b = int(input("Enter B: "))
temp = a
a = b
b = temp
print("A =", a)
print("B =", b)


# Program-10 :- Student Details (Mini Challenge)

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
age = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))

print("\n----- Student Details -----")
print(f"Name       : {name}")
print(f"Roll Number : {roll_no}")
print(f"Branch      : {branch}")
print(f"Age         : {age}")
print(f"CGPA        : {cgpa}")