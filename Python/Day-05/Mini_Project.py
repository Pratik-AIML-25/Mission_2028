'''
✨ATM Login System

User enters:
PIN

Correct PIN:
1234

If correct:
Welcome to ATM

Else:
Invalid PIN                                                                                                        '''

# CODE👇
pin = input("Enter your PIN: ")

if pin == "1234":
    print("Welcome to ATM")
else:
    print("Invalid PIN")