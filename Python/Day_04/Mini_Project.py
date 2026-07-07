'''Student Result Calculator

   Take input for four subjects:

   English
   Maths
   Science
   Computer

   Calculate:

   Total Marks
   Percentage

   Example:

   English : 90
   Maths : 80
   Science : 95
   Computer : 88

   Total : 353
   Percentage : 88.25%                                                                                         '''


# CODE👇

english = int(input("Enter English marks: "))
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
computer = int(input("Enter Computer marks: "))

total = english + maths + science + computer
percentage = total / 4

print("\n----- Result -----")
print("Total Marks =", total)
print(f"Percentage = {percentage:.2f}%")