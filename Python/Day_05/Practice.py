# Program-1 :- Positive or Negative Number

# CODE👇
num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")


# Program-2 :- Even or Odd

# CODE👇
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Program-3 :- Voting Eligibility

# CODE👇
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")


# Program-4 :- Largest of Two Numbers

# CODE👇
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Largest Number =", num1)
elif num2 > num1:
    print("Largest Number =", num2)
else:
    print("Both numbers are equal")


# Program-5 :- Smallest of Two Numbers

# CODE👇
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 < num2:
    print("Smallest Number =", num1)
elif num2 < num1:
    print("Smallest Number =", num2)
else:
    print("Both numbers are equal")


# Program-6 :- Pass or Fail (Marks >= 33)

# CODE👇
marks = int(input("Enter your marks: "))

if marks >= 33:
    print("Pass")
else:
    print("Fail")


# Program-7 :- Check Divisible by 5

# CODE👇
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")


# Program-8 :- Check Divisible by 7

# CODE👇
num = int(input("Enter a number: "))

if num % 7 == 0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")


# Program-9 :- Greatest of Three Numbers

# CODE👇
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Greatest Number =", num1)
elif num2 >= num1 and num2 >= num3:
    print("Greatest Number =", num2)
else:
    print("Greatest Number =", num3)


# Program-10 :- Check Leap Year (simple logic)

# CODE👇
year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# Program-11 :- Check Number is Zero

# CODE👇
num = int(input("Enter a number: "))

if num == 0:
    print("Number is Zero")
else:
    print("Number is Not Zero")


'''Program-12 :- 

Age Category
Child
Teen
Adult
Senior                                                                                                            '''

# CODE👇
age = int(input("Enter your age: "))

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 59:
    print("Adult")
else:
    print("Senior")


''' Program-13 :- 

Temperature Checker
Cold
Normal
Hot                                                                                                                '''

# CODE👇
temp = int(input("Enter temperature: "))

if temp < 20:
    print("Cold")
elif temp <= 35:
    print("Normal")
else:
    print("Hot")


''' Program-14 :- 

Grade Calculator
90+  A
75+  B
60+  C
40+  D
Else Fail                                                                                                         '''

# CODE👇
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


''' Program-15 :- 

Password Checker

Correct password:

    python123

Output:

    Access Granted

Otherwise:

    Access Denied                                                                                                 '''

# CODE👇
password = input("Enter password: ")

if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")