'''
Student Result Analyzer

Take input:
Name
Physics Marks
Chemistry Marks
Maths Marks

Calculate:
Total
Percentage

Then print:
===== RESULT =====
Name : Pratik
Total : 255
Percentage : 85%
Grade : A

Grade Rules:
90+ → A+
80+ → A
70+ → B
60+ → C
40+ → D
Else → Fail                                                                                                                                  '''


# CODE👇
name = input("Enter your name: ")
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
maths = int(input("Enter Maths marks: "))

total = physics + chemistry + maths
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\n===== RESULT =====")
print("Name :", name)
print("Total :", total)
print(f"Percentage : {percentage:.2f}%")
print("Grade :", grade)