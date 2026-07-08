'''
TOPIC :- Conditional Statements (if, elif, else)


1. if Statement

CODE👇
age = 20

if age >= 18:
    print("You can vote")


2. if-else

CODE👇
age = 15

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


3. if-elif-else

CODE👇
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


4. Nested if

CODE👇
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible")
    else:
        print("Not Citizen")
else:
    print("Under Age")


5. Short Hand if

CODE👇
age = 20

if age >= 18: print("Adult")

'''