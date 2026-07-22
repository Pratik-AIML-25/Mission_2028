''' Password Strength Checker

    Take a password as input and check:
    Minimum 8 characters.
    Contains at least one digit.
    Contains at least one uppercase letter.

    Output:
    Strong Password
    or
    Weak Password                                                                                                                             '''

# CODE👇
password = input("Enter your password: ")
if (len(password) >= 8 and
    any(char.isdigit() for char in password) and
    any(char.isupper() for char in password)):
    print("Strong Password")
else:
    print("Weak Password")


''' Example-1:-
    Input:- Enter your password: Pratik123
    Output:- Strong Password
    
    Example-2
    Input:- Enter your password: password
    Output:- Weak Password                                                                                                                    '''